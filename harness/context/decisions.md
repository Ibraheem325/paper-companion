# Decisions log

New decisions made while building. The founding decisions (#1–#2) live in
`../docs/design.md` §4; this file continues the numbering.

Add an entry when we pick one option over another (a model, a library, a
chunk size, a metric). Never delete an entry; if we change our minds, add a
new one that says "replaces #N".

| # | Date | Step | Decision | Why | Alternatives considered |
|---|---|---|---|---|---|
| 3 | 2026-11-11 | 1 | Use `HuggingFaceTB/SmolLM2-135M` (base) for the by-hand transformers lessons | Tiny (~0.5 GB in memory), fast on the 8 GB M1, made by Hugging Face, Llama-style tokenizer | GPT-2 (124M) |
| 4 | 2026-11-11 | 2 | Keep each math formula once, as its LaTeX source (`alttext`) wrapped in `$…$` | LaTeXML stores math twice (visual + LaTeX); LLMs read LaTeX well; saved ~800 chars in one section | Keep the visual Unicode version; drop math entirely |
| 5 | 2026-11-11 | 2 | Remove figures (`ltx_figure`) from section text; keep tables | Captions were mixed into the text before the first real sentence; tables hold the results numbers | Keep captions inline; store captions separately |
| 6 | 2026-11-11 | 2 | Skip references and appendices for now (abstract + `ltx_section` only) | Keep Step 2 simple; revisit when retrieval quality is measured (Steps 5–6) | Include them from the start |
| 7 | 2026-11-11 | 2 | PDF fallback (PyMuPDF) splits by page, `source: "pdf"` | A PDF has no section tags; pages still give citable locations | Guess headings with regex; one big "full text" section |
