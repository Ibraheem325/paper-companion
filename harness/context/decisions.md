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
| 8 | 2026-11-12 | 3 | Embedding model: `BAAI/bge-small-en-v1.5` (384 dims) via sentence-transformers | Reads up to 512 tokens so 200-word chunks aren't cut; small (~130 MB), fast on the 8 GB M1 | `all-MiniLM-L6-v2` (256-token limit would truncate chunks) |
| 9 | 2026-11-12 | 3 | Chunks: 200 words, 40-word overlap, never crossing a section border | Overlap keeps border sentences whole; one section per chunk keeps citations exact | No overlap; token-based chunk sizes |
| 10 | 2026-11-12 | 3 | Add bge's query instruction prefix to questions only (not chunks) | Recommended by the model card; moved the right chunk from #3 to #1 on one test question (to be measured in Step 5) | No prefix |
| 11 | 2026-11-12 | 3 | Store the index as `.npy` (vectors) + `.json` (chunks) in `data/index/`; plain NumPy dot-product search | Learn the mechanics without frameworks; tiny index per paper | A vector database (FAISS, Chroma), revisit if many papers |
| 12 | 2026-11-14 | 4 | Model file: `bartowski/Llama-3.2-3B-Instruct-GGUF:Q4_K_M`, context 4096 | ~2 GB fits the 8 GB M1; the full 128k context would need far more memory | Other quantizations (Q8, Q3) |
| 13 | 2026-11-14 | 4 | Server on fixed port 8080; app reads `LLM_URL` (env var) | A stable address; switching engines is a config change (decision #1) | Random port each launch |
| 14 | 2026-11-14 | 4 | Call the server with plain `httpx`, no SDK | Already a dependency; framework-free like Step 3 | `openai` Python SDK |
| 15 | 2026-11-14 | 4 | Keep LaTeX in the index; strip `$…$` only in answers (`plain_math`) | The model reads LaTeX fine; re-indexing not needed | Strip at ingestion; ask the model in the prompt |
| 16 | 2026-11-14 | — | Dashboard chat may also edit `harness/site/**` | Lets Claude fix the dashboard directly | Paste every change by hand |
