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
| `site/index.html` | A one-page dashboard of your progress and notes |

## Use it

**Ask questions.** Two separate steps:

1. In your terminal, start Claude inside `harness/`:
   ```bash
   cd paper-companion/harness
   claude
   ```
2. Wait for Claude's own input box to appear, then type this **into Claude**,
   not into the terminal:
   ```
   /kb-answer what's the current step, and what do I do next?
   ```

**After a coding session:** `/kb-sync`

**See the dashboard** (serve from the repo root so the page can read `docs/`):

```bash
cd paper-companion
python3 -m http.server 8000
# open http://localhost:8000/harness/site/
```

Type a question on the page, click **Copy command**, and paste it into Claude.
