# Progress

Where I am *inside* the current step. The step number itself lives at the top
of `../docs/design.md`; update both when a step is finished.

Last synced commit: (none yet; run `/kb-sync`)

## Current step: 2, Fetch one arXiv paper and split it by section

**Goal:** fetch one arXiv paper (HTML first, PDF fallback) and split it into
sections.

**Done so far:**
- (nothing yet)

**Next action:**
- (decide with the tutor)

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
| 2026-11-11 | 1 ✅ | Installed transformers + torch; notebook: tokenizer, logits, softmax, greedy + sampling loops, compared with `generate()` | Tokens & subwords; logits → softmax; one token per run, fed back in; greedy repeats, temperature adds randomness; KV cache can flip near-ties. Colab is paid (200 units/month) |
| 2026-10-22 | 0 | Finished the project skeleton (`uv init`) and wrote the design doc | — |
