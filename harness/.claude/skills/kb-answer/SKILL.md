---
name: kb-answer
description: Answer a question about the Paper Companion project (progress, a concept, a past decision, an error, or a code review) from the design doc, the repo, the context notes and official docs, with citations and in my teaching style. Use whenever I ask a project or learning question.
argument-hint: <your question, error output, or "review my code">
---

# kb-answer

Question: $ARGUMENTS

If the question is empty, ask me what I want to know and stop.

## 1. Classify the question

Pick exactly one type. If two fit, pick the first in this list.

| Type | Signals |
|---|---|
| **error** | A traceback, error message, or "it doesn't work" |
| **review** | "review", "look at my code", "is this right?" |
| **progress** | "where am I", "what's next", "current step" |
| **decision** | "why did we choose…", "why not…" |
| **concept** | "what is…", "explain…", "how does … work" |

Say the type in one line: `Type: concept`.

## 2. Gather evidence (trust order; stop when you have enough)

1. `../docs/design.md`: always skim the "Current step" line and the relevant section.
2. `context/progress.md`, `context/decisions.md`, `context/glossary.md`.
3. The repo code under `../`. Use Grep/Glob to find it; read only what you need.
4. Official docs from `context/sources.md`, only to explain or verify a technology.

Per type:

- **progress:** design doc build order + `progress.md`. Name the current step, what's done inside it, and ONE next action.
- **concept:** check `glossary.md` first. Then fetch ONE official docs page for accuracy. Tie the concept to the build step where it's used.
- **decision:** quote the design doc §4 or `decisions.md`. If the decision isn't recorded, say so and don't invent a reason. You may offer general trade-offs, clearly labelled as not-my-decision.
- **error:** if the full traceback or the command that produced it is missing, ask for it before guessing. Read the code at the lines the traceback names. Check hardware limits (8 GB M1, no CUDA on the Mac).
- **review:** run `git status`, `git diff`, and `git log --oneline -5` to find what changed. Review only those changes. Check them against the design doc's structure and current step.

## 3. Answer in this shape

```
**Short answer:** 1–2 lines.

<Details: bullets or a table. Define each new term in one plain sentence plus an
analogy. For error: Cause → How to confirm → Fix → What it teaches.
For review: a table | Severity | File:line | Issue | Why it matters |, then what's good.>

**Try this:** one small experiment or next action (predict → run → compare).

**Sources:** `path/file.py:12`, `../docs/design.md` §4, https://…
```

Rules:
- Every claim about my project cites a file. Every claim about a technology cites the repo or a docs URL.
- If the sources don't answer it: "I don't know from the sources." Then say where to look.
- Don't write full solutions unless I asked. Hints, then pseudocode, then code.
- Keep it to one step. Don't preview later steps unless I ask.

## 4. Offer note updates (don't write them yet)

If the answer revealed a new term, a decision, or progress, end with a short list:
"Want me to add these? → glossary: *KV cache*; progress: *tokenizer loaded ✅*".
Write them only after I say yes.
