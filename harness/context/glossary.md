# Glossary

Terms I've learned, in my own words. Add a term the first time it comes up in a
step. Keep each definition to 1–2 plain sentences, plus where it shows up in
Paper Companion.

| Term | Plain-English meaning | Where it shows up in the project | First met in step | Official link |
|---|---|---|---|---|
| Tokenizer | Turns text into a list of numbers (token IDs) the model can read, and back again. Each model has its own. | Step 1 notebook (`tok`); later counts how much paper text fits in the model | 1 | https://huggingface.co/docs/transformers/main_classes/tokenizer |
| Token ID | The number for one piece of text: its position in the vocabulary. `Ġreads` → 12927. | Step 1 notebook, `input_ids` | 1 | https://huggingface.co/docs/transformers/main_classes/tokenizer |
| Vocabulary | The fixed list of all pieces a tokenizer knows (`vocab.json`). `Ġ` in a piece means "space before it". | Downloaded with SmolLM2's tokenizer | 1 | https://huggingface.co/learn/llm-course/chapter2/4 |
| Subword tokenization | Words not in the vocabulary get built from smaller known pieces, like Lego bricks: "Ibraheem" → `I` `bra` `he` `em`. | Papers have many rare terms, so they cost more tokens (matters for chunking in Step 3) | 1 | https://huggingface.co/learn/llm-course/chapter2/4 |
| Logits | The model's raw score for every token in the vocabulary as the next token. Shape `[sentences, tokens, vocab]`. | Step 1 notebook: `[1, 5, 49152]` | 1 | https://huggingface.co/docs/transformers/llm_tutorial |
| Softmax | Turns raw scores into percentages that add up to 100%; small score gaps become big probability gaps. | Step 1: `' the'` 26%, `' Paris'` 8% | 1 | https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.softmax.html |
| Autoregressive generation | The model predicts one token per run; you append it and run again, because the model has no memory between runs. | Step 1 hand-written loop; `model.generate()`; llama.cpp in Step 4 | 1 | https://huggingface.co/docs/transformers/llm_tutorial |
| Greedy decoding | Always pick the single highest-scoring token (`argmax`). Deterministic; prone to repetition loops. | Step 1: "department of department of…" | 1 | https://huggingface.co/docs/transformers/generation_strategies |
| Sampling | Pick the next token at random, weighted by its probability, like a raffle (`torch.multinomial`). Breaks loops. | Step 1 sampling loop | 1 | https://huggingface.co/docs/transformers/generation_strategies |
| Temperature | Divides logits before softmax: below 1 = safer/more focused, above 1 = wilder/more random. | Step 1 sampling loop (0.6, 0.8, 1.0) | 1 | https://huggingface.co/docs/transformers/generation_strategies |
| Attention mask | 1 = real token, 0 = padding to ignore. Built by the tokenizer by simple counting; a hard filter, not a belief. | Step 1 `inputs`; matters when batching chunks in Step 3 | 1 | https://huggingface.co/docs/transformers/glossary#attention-mask |
| Padding | Filler tokens added so all sentences in a batch have the same length. | Batching chunks in Step 3 | 1 | https://huggingface.co/docs/transformers/pad_truncation |
| KV cache | The model remembers its work on earlier tokens so each new run only processes the new token. Same maths, slightly different rounding. | Step 1: `use_cache=False` made `generate()` match the hand loop; central to Step 10 | 1 | https://huggingface.co/docs/transformers/llm_tutorial |
| HTML parsing / BeautifulSoup | Reading a web page into a searchable tree so you can grab parts by tag ("every `ltx_section`") and keep only the text. | `fetch_html()` in `src/paper_companion/ingest/arxiv.py` | 2 | https://www.crummy.com/software/BeautifulSoup/bs4/doc/ |
| LaTeXML | The tool arXiv uses to turn authors' LaTeX into HTML. Gives every paper the same tags (`ltx_section`, `ltx_abstract`, `<math alttext=…>`). | Why splitting arXiv HTML is reliable | 2 | https://info.arxiv.org/about/accessible_HTML.html |
| JSON | A plain-text format for structured data (lists, key–value records). | Papers saved to `data/papers/<id>.json` | 2 | https://docs.python.org/3/library/json.html |
| PDF fallback / PyMuPDF | If the HTML download fails, read the PDF instead. PyMuPDF extracts text per page but can't tell headings, math or captions apart. | `fetch_pdf()`; split by page (decision #7) | 2 | https://pymupdf.readthedocs.io |
| Chunk & overlap | A small window of text (200 words) cut from a section; neighbouring chunks share 40 words so a sentence on the border stays whole in one of them. | `chunk_words()` in `index/vectors.py` | 3 | https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html |
| Embedding | A fixed-size list of numbers (384 for bge-small) that represents a text's meaning; similar meanings sit close together, like GPS coordinates for meaning. | `build_index()`, shape `[29, 384]` | 3 | https://sbert.net |
| Cosine similarity / dot product | How close two vectors point; with length-1 vectors it's just multiply-and-add (`@`). 1 = same meaning, 0 = unrelated. Ranking matters, not the raw score. | `search()` in `retrieve/search.py` | 3 | https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html |
| Top-k | Return the k best-scoring chunks, not just #1, because the right chunk is often close behind. | `search(..., k=3)` | 3 | https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html |
| Query instruction prefix | A fixed sentence bge expects before a search question ("Represent this sentence for searching relevant passages: "). | `QUERY_PREFIX` (decision #10) | 3 | https://huggingface.co/BAAI/bge-small-en-v1.5 |
| Kernel (notebook) | The Python process behind a notebook that holds your variables; restarting or renaming the notebook wipes them, even if old outputs still show. | "chunks is not defined" after renaming | 3 | https://code.visualstudio.com/docs/datascience/jupyter-notebooks |
| Compute unit | Colab's paid-plan currency: a runtime drains units per hour while connected, and bigger GPUs drain faster (per-hour rates not yet verified; check the Resources panel). When they run out you drop back to the free tier. | My Colab budget: 200/month, spent on GPU steps (e.g. 9, 10) | 1 | https://research.google.com/colaboratory/faq.html |
