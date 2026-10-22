---
name: kb-sync
description: Refresh the Paper Companion harness after I've worked on the repo. Pull the latest changes, see what's new since the last sync, propose updates to the progress, decisions and glossary notes, and check the harness files agree with each other. Use when I say sync, refresh, or "I just pushed".
argument-hint: (no arguments)
---

# kb-sync

Goal: make the `context/` notes match what's actually in the repo. **Propose
everything, write nothing until I approve.**

## 1. Get the latest

1. `git fetch` and `git status`.
2. If the branch is behind its remote, show the incoming commits
   (`git log --oneline HEAD..@{u}`) and ask before running `git pull`.
3. If there are uncommitted changes, list them. They count as "work in progress";
   don't stash or discard them.

## 2. Find what changed since the last sync

1. Read the `Last synced commit:` line in `context/progress.md`.
2. Run `git log --oneline --stat <that-commit>..HEAD`. If the line is missing or
   the commit can't be found, use the last 20 commits.
3. Read the diffs that matter: code under `../src`, `../eval`, `../notebooks`,
   `../deploy`; `../pyproject.toml`; `../docs/design.md`. Skip lockfiles and data.

## 3. Draft the updates

| Note | Propose an update when… |
|---|---|
| `context/progress.md` | Work moved the current step forward: add to "Done so far", set "Next action", add one log row |
| `context/decisions.md` | A commit picked one option over another: a new dependency in `pyproject.toml`, a model name, a chunk size, a metric. Ask me for the "why" if the commit doesn't say. |
| `context/glossary.md` | A new technical term appears in the code or commit messages that isn't in the glossary yet |
| `../docs/design.md` | The current step looks finished. **Ask** me; never decide a step is done on my behalf. |

## 4. Consistency checks

Report each as ✅ or ⚠️ with a one-line fix:

- "Current step" in the design doc matches `progress.md`.
- Every domain in `context/sources.md` has a matching `WebFetch(domain:…)` rule in
  `.claude/settings.json`, and the other way round.
- No folder exists ahead of its build step (design doc §5: "create each folder only
  when its step arrives").
- Each dependency in `pyproject.toml` maps to a technology in design doc §2.

## 5. Show, then write

Show one summary:

```
Changes since <old-sha> → <new-sha>: N commits, M files

Proposed updates
| File | Change |
|---|---|

Checks
✅ / ⚠️ …
```

Ask: "Apply all, some (which?), or none?" Apply only what I approve. Then set
`Last synced commit:` in `progress.md` to the current `HEAD` short hash. Don't
commit or push unless I ask.
