# Paper Companion: Design Doc

> **Status: DRAFT.** Lines marked `TODO` haven't been decided yet. Treat them as
> unknown, not as decisions.

## 1. Idea

A research-paper assistant: give it papers, then ask questions about them and
get answers grounded in the papers' text.

The real goal is **learning**. Each part of the app is a reason to learn one
technology hands-on. Finishing fast is not the goal.

- TODO: Who uses it? (Just me?)
- TODO: What does "done" look like for v1? (e.g. "ask a question about 1 PDF, get a cited answer")

## 2. Technologies to learn

| Area | Technology | Role in the project |
|---|---|---|
| Retrieval | RAG (embeddings, vector store, reranker) | TODO |
| Models | Hugging Face transformers | TODO |
| Orchestration | LangChain / LangGraph | TODO |
| Quality | Evaluation | TODO |
| Packaging | Docker / Kubernetes | TODO |
| Serving (GPU) | vLLM, SGLang | TODO |
| Serving (local) | llama.cpp / Llama | TODO |

## 3. Hardware

| Machine | Specs | Used for |
|---|---|---|
| MacBook | M1, 8 GB RAM | Local development; llama.cpp (small quantized models) |
| Google Colab | Free tier (GPU) | vLLM (needs an NVIDIA GPU) |

## 4. Decisions

| # | Decision | Why | Date |
|---|---|---|---|
| 1 | llama.cpp on the Mac, vLLM on Colab | TODO: write down the reason in my own words | TODO |
| 2 | Python ≥ 3.12, managed with `uv` | Set up by `uv init` (see `pyproject.toml`) | TODO |

## 5. Structure

- TODO: folders/modules (e.g. `ingest/`, `retrieve/`, `generate/`, `eval/`)

## 6. Build order

- [x] Step 0: Project skeleton (`uv init`)
- [ ] TODO: Step 1 …
