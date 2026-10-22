"""Dashboard server: serves the page and answers chat messages through Claude Code.

Run from anywhere:  uv run python harness/site/server.py
Then open:          http://localhost:8000/harness/site/

Each chat message runs `claude -p` inside harness/, so it uses your own Claude
login, CLAUDE.md, skills and settings. Claude may read the repo and edit only
the notes (harness/context/ and docs/design.md); everything else is denied.
"""

import json
import shutil
import subprocess
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

PORT = 8000
HARNESS = Path(__file__).resolve().parent.parent
REPO = HARNESS.parent
TIMEOUT_S = 600


def allowed_tools() -> list[str]:
    """The harness's own allow-list, plus edits to the notes files only.

    Passed on the command line so it applies even before the folder is trusted.
    """
    settings = json.loads((HARNESS / ".claude" / "settings.json").read_text())
    rules = settings.get("permissions", {}).get("allow", [])
    return rules + [
        "Read", "Grep", "Glob",
        f"Edit(/{HARNESS}/context/**)",
        f"Edit(/{REPO}/docs/design.md)",
    ]


def ask_claude(message: str, session_id: str | None) -> dict:
    claude = shutil.which("claude")
    if not claude:
        return {"error": "The `claude` command wasn't found. Install Claude Code, then restart this server."}

    cmd = [
        claude, "-p", message,
        "--output-format", "json",
        "--add-dir", str(REPO),
        "--allowedTools", *allowed_tools(),
    ]
    if session_id:
        cmd += ["--resume", session_id]

    try:
        proc = subprocess.run(cmd, cwd=HARNESS, capture_output=True, text=True,
                              timeout=TIMEOUT_S, stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        return {"error": f"Claude didn't answer within {TIMEOUT_S // 60} minutes."}

    try:
        out = json.loads(proc.stdout)
    except json.JSONDecodeError:
        detail = (proc.stderr or proc.stdout).strip()[-1500:]
        return {"error": f"Claude exited without an answer.\n\n{detail}"}

    if out.get("is_error"):
        return {"error": out.get("result") or "Claude reported an error.", "session_id": out.get("session_id")}
    return {"answer": out.get("result", ""), "session_id": out.get("session_id")}


class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/api/ask":
            self.send_error(404)
            return
        # Only accept requests from this dashboard, not from other websites.
        origin = self.headers.get("Origin", "")
        if origin and origin not in (f"http://localhost:{PORT}", f"http://127.0.0.1:{PORT}"):
            self.send_error(403)
            return

        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length) or b"{}")
            message = str(body.get("message", "")).strip()
        except (ValueError, json.JSONDecodeError):
            self.send_error(400)
            return
        if not message:
            self.send_error(400, "Empty message")
            return

        print(f"→ asking Claude: {message[:80]!r}", flush=True)
        result = ask_claude(message, body.get("session_id") or None)

        data = json.dumps(result).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def end_headers(self):
        # Always serve fresh notes.
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        if self.command == "POST":
            super().log_message(fmt, *args)


def main():
    server = ThreadingHTTPServer(("127.0.0.1", PORT), partial(Handler, directory=str(REPO)))
    print(f"Dashboard: http://localhost:{PORT}/harness/site/   (Ctrl+C to stop)", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        sys.exit(0)


if __name__ == "__main__":
    main()
