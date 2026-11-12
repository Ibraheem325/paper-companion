# Progress

Where I am *inside* the current step. The step number itself lives at the top
of `../docs/design.md`; update both when a step is finished.

Last synced commit: (none yet; run `/kb-sync`)

## Current step: 4, Answer with Llama 3.2 3B via a llama.cpp server, with citations

**Goal:** run Llama 3.2 3B locally through llama.cpp, give it the top chunks,
and get answers that cite the section they came from.

**Done so far:**
- (nothing yet)

**Next action:**
- (decide with the tutor)

## Finished: Step 3, Chunk, embed, vector search (without frameworks) ✅ (2026-11-12)

Modules: `src/paper_companion/index/vectors.py` (chunk, embed, save/load) and `src/paper_companion/retrieve/search.py` (`search()`). Notebook: `04_chunk_embed.ipynb`. Index saved in `data/index/`.
- 1706.03762 → 29 chunks (200 words, 40 overlap, per section; decision #9) → vectors `[29, 384]` with bge-small (decision #8)
- "What are end-to-end memory networks based on?": right chunk (Background #1) ranked #3 without the prefix, #1 with bge's query prefix (decision #10); scores bunch together (~0.68–0.73), so rank matters, not score
- "How many layers does the encoder have?": answer (`$N=6$`) in the #1 chunk
- Lessons: dilution (one answer sentence in a 200-word chunk), top-k, one question is an anecdote → measure in Step 5

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
- PDF fallback is basic (PyMuPDF, split by page); compare better parsers in Step 7

---

## Log

Newest first. One line per session: date, what I tried, what I learned.

| Date | Step | What I did | What I learned |
|---|---|---|---|
| 2026-11-12 | 3 ✅ | Chunked a paper, embedded with bge-small, searched by cosine similarity, tried the query prefix, moved it into `index/` + `retrieve/` | Chunks & overlap; embeddings = one fixed-size vector per chunk; dot product of normalized vectors; rank over score; kernel restarts wipe variables |
| 2026-11-11 | 2 ✅ | Fetched arXiv HTML, split by section, cleaned text, tested a 2nd paper, moved code into `ingest/arxiv.py`, added PDF fallback | Why HTML beats PDF (structure, LaTeX); parsers leave junk (captions, duplicated math) you must inspect; notebook → module |
| 2026-11-11 | 1 ✅ | Installed transformers + torch; notebook: tokenizer, logits, softmax, greedy + sampling loops, compared with `generate()` | Tokens & subwords; logits → softmax; one token per run, fed back in; greedy repeats, temperature adds randomness; KV cache can flip near-ties. Colab is paid (200 units/month) |
| 2026-10-22 | 0 | Finished the project skeleton (`uv init`) and wrote the design doc | — |
