# Progress

Where I am *inside* the current step. The step number itself lives at the top
of `../docs/design.md`; update both when a step is finished.

Last synced commit: (none yet; run `/kb-sync`)

## Current step: 3, Chunk, embed, vector search (without frameworks)

**Goal:** cut the sections into chunks, turn them into embeddings, and search
them by similarity, all by hand.

**Done so far:**
- (nothing yet)

**Next action:**
- (decide with the tutor)

## Finished: Step 2, Fetch an arXiv paper and split it by section ✅ (2026-11-11)

Module: `src/paper_companion/ingest/arxiv.py` → `fetch_paper(arxiv_id)` (HTML first, PDF fallback). Notebooks: `02_ingest.ipynb`, `03_testing.ipynb`.
- HTML page ~490k chars, mostly markup; LaTeXML tags make sections easy to find
- Cleaning: removed figure captions and repeated titles, squeezed whitespace (decision #5)
- Tested on 2410.22360 (arxivDIGESTables) and 1706.03762 (Attention Is All You Need)
- Math was duplicated (visual + LaTeX) → kept once as LaTeX (decision #4); empty sections skipped
- Abstract included; references and appendices skipped for now (decision #6)
- PDF fallback with PyMuPDF, split by page (decision #7); PDF text readable but loses headings, subscripts and has line-break noise
- First paper saved to `data/papers/2410.22360.json`; `data/` is gitignored

## Finished: Step 1, Tokens and transformers by hand ✅ (2026-11-11)

All in `notebooks/01_tokens.ipynb`, with SmolLM2-135M (decision #3):
- Tokenizer: "Paper Companion reads arXiv papers." → 6 tokens; "Ibraheem uses tokenization." → 8 (rare name split into 4 pieces)
- Logits: shape `[1, 5, 49152]` = sentences × tokens × vocabulary; top next token after "The capital of France is" = `' the'` (26%), `' Paris'` 8%
- Greedy loop (25 tokens) fell into a repetition loop ("department of department of…")
- Sampling with temperature breaks loops; results change run to run
- `model.generate()` matched the loop until a near-tie; with `use_cache=False` it matched exactly (KV cache rounding)

**Open questions:**
- (none yet)

---

## Log

Newest first. One line per session: date, what I tried, what I learned.

| Date | Step | What I did | What I learned |
|---|---|---|---|
| 2026-11-11 | 2 ✅ | Fetched arXiv HTML, split by section, cleaned text, tested a 2nd paper, moved code into `ingest/arxiv.py`, added PDF fallback | Why HTML beats PDF (structure, LaTeX); parsers leave junk (captions, duplicated math) you must inspect; notebook → module |
| 2026-11-11 | 1 ✅ | Installed transformers + torch; notebook: tokenizer, logits, softmax, greedy + sampling loops, compared with `generate()` | Tokens & subwords; logits → softmax; one token per run, fed back in; greedy repeats, temperature adds randomness; KV cache can flip near-ties. Colab is paid (200 units/month) |
| 2026-10-22 | 0 | Finished the project skeleton (`uv init`) and wrote the design doc | — |
