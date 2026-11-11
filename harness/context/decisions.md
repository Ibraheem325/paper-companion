# Decisions log

New decisions made while building. The founding decisions (#1–#2) live in
`../docs/design.md` §4; this file continues the numbering.

Add an entry when we pick one option over another (a model, a library, a
chunk size, a metric). Never delete an entry; if we change our minds, add a
new one that says "replaces #N".

| # | Date | Step | Decision | Why | Alternatives considered |
|---|---|---|---|---|---|
| 3 | 2026-11-11 | 1 | Use `HuggingFaceTB/SmolLM2-135M` (base) for the by-hand transformers lessons | Tiny (~0.5 GB in memory), fast on the 8 GB M1, made by Hugging Face, Llama-style tokenizer | GPT-2 (124M) |
