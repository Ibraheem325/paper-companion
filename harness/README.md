# Paper Companion Knowledge Harness

A tutor for this project. It answers from the design doc, the code, your notes,
and official docs, one step at a time.

## What's here

| Path | What it is |
|---|---|
| `CLAUDE.md` | The rules Claude follows every time it starts in this folder |
| `context/` | Your notes: progress, decisions, glossary, allowed sources |
| `.claude/settings.json` | What Claude may read without asking: the repo, read-only git, the docs sites |
| `.claude/skills/kb-answer/` | `/kb-answer <question>`: answers with citations |
| `.claude/skills/kb-sync/` | `/kb-sync`: refreshes the notes after you've pushed work |
| `site/` | The dashboard: your progress and notes, plus a chat with your tutor (`server.py` runs it) |

## Use it

### The dashboard: viewer and chat in one page

```bash
cd ~/paper-companion
uv run python harness/site/server.py
# open http://localhost:8000/harness/site/
```

- **Ask** in the "Ask your tutor" box. Enter sends, Shift+Enter adds a new line.
  The first message uses `/kb-answer`, and follow-ups continue the same conversation.
- **New chat** starts a fresh conversation. **Sync notes** runs `/kb-sync`.
- Answers come from Claude Code on your Mac (your login, rules and skills).
  From the page, Claude can read the repo but may only edit your notes
  (`harness/context/` and `docs/design.md`), never your code.
- Stop the server with **Ctrl + C**.

### Or in the terminal

1. Start Claude inside `harness/`:
   ```bash
   cd ~/paper-companion/harness
   claude
   ```
2. Wait for Claude's input box, then type this **into Claude**, not into the terminal:
   ```
   /kb-answer what's the current step, and what do I do next?
   ```

After a coding session, run `/kb-sync` (or click **Sync notes** on the dashboard).
