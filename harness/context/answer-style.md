# Answer style

How every answer to me should look. This wins over any other formatting rule
in the harness (CLAUDE.md, skills). Keep answers short and never overwhelming:
no walls of bullets, no extra sections.

## 1. Steps (anything I have to do)

One block per step, separated by `---`. No explanations of basic tool mechanics
(how to run a notebook cell, press ⇧↵, click "+ Code"); just give the code.

````
---

### Step N · Short title
*Why: 1–2 informative sentences: what this step does AND why it matters for
the project or what I'm learning.*
```python
code or command
```
> Optional one-line note, only if really needed.

---

🎯 What to send back (e.g. "Send me what Cell 2 prints").
````

## 2. Explanations (concepts, "what is", "why")

At most 4 short blocks, separated by `---`. No long bullet lists.

```
### 💡 In one line
The definition in one sentence.

---

### 🧩 Think of it like…
One analogy.

---

### 🔍 In your project
Where it shows up, ideally using my own output.

---

### 📖 Learn more (optional)
One official docs link. Always last.
```

## 3. Errors

Name the mistake in one line and give the corrected line or command. No
"how to confirm" or "what it teaches" walkthrough for typos, syntax slips or
copy-paste mistakes.

## 4. General

- Anything I have to paste goes in its own fenced code block with a language tag
  (```` ```python ````, ```` ```bash ````, ```` ```markdown ````), one block per paste, nothing
  else inside it, so the UI shows a copy button and I can copy it in one click.

- Sources: still cite, but compactly at the end (one line), not inline everywhere.
- Note updates (progress, glossary, decisions): offer them in one short line at the end.
