# Paper Companion: Design Doc

**Current step: 1** (see [Build order](#6-build-order))

## 1. Idea

A research-paper assistant: give it an arXiv paper, then ask questions about
it and get answers grounded in the paper's text.

The real goal is **learning**. Each part of the app is a reason to learn one
technology hands-on. Finishing fast is not the goal.

**Users:** me first, for literature reviews in computer science. Later,
possibly other researchers. Users are technical.

**v1 is done when**, given an arXiv ID, the app:

- answers questions about that paper, citing the section each answer came from;
- answers "not reported in the paper" when the information isn't there;
- runs locally on my M1 with Llama 3.2 3B through llama.cpp;
- has a measured score on a QASPER subset (a benchmark of questions about NLP papers).

This corresponds to the end of **Step 5** in the build order.

## 2. Technologies to learn

| Technology | Role in the app |
|---|---|
| Hugging Face + transformers | Embedding models, reranker, evidence-checking model; loading datasets (QASPER) |
| Llama (via llama.cpp) | The LLM that reads and answers; Llama 3.2 3B at 4-bit on the Mac |
| vLLM | Fast serving and structured JSON output for paper cards; benchmarked on Colab |
| SGLang | Many questions about the same paper, reusing the shared paper text (prefix caching); benchmarked on Colab against vLLM |
| RAG | Split → embed → retrieve → rerank → answer with citations; the backbone of every feature |
| LangChain + LangGraph | LangChain for standard components; LangGraph for answer → verify → retry loops |
| Evaluation | QASPER (Q&A), ArxivDIGESTables (comparison tables), PDF-parser accuracy, my own labelled papers |
| Docker + Kubernetes | Package the services and run them on a local cluster; the LLM stays outside the cluster on the Mac |

## 3. Hardware

| Machine | Specs | Used for |
|---|---|---|
| MacBook | M1, 8 GB RAM | Local development; llama.cpp (small 4-bit models) |
| Google Colab | Free tier (NVIDIA GPU) | vLLM and SGLang benchmarks |

## 4. Decisions

| # | Decision | Why |
|---|---|---|
| 1 | llama.cpp on the Mac; vLLM and SGLang on Colab | See below |
| 2 | Python ≥ 3.12, managed with `uv` | Set up by `uv init` (see `pyproject.toml`) |

**Why llama.cpp on the Mac and vLLM/SGLang on Colab:**

- The M1 has 8 GB of memory shared by CPU and GPU. macOS uses 3–4 GB, so only
  small 4-bit models (1B–3B) fit.
- llama.cpp is the most mature engine for Apple Silicon and 4-bit models.
- vLLM and SGLang need an NVIDIA GPU for real performance. On the Mac, vLLM's
  memory management (paged attention) is experimental, and SGLang reportedly
  lacks prefix-cache reuse, which is the feature we care about.
- Docker on a Mac can't access the GPU, so the LLM runs natively on the Mac,
  outside the containers.
- Free Colab GPUs aren't always available, so Colab is used as a lab for
  benchmarks, never as a server.
- Every engine exposes the same OpenAI-compatible API. The app only knows a
  URL, so switching engines is a configuration change, not a code change.

## 5. Structure

Create each folder only when its step arrives.

```
paper-companion/
├── docs/design.md
├── src/paper_companion/
│   ├── ingest/     # fetch arXiv HTML/PDF, parse, split into sections
│   ├── index/      # embeddings, vector store
│   ├── retrieve/   # search, hybrid search, reranker
│   ├── generate/   # prompts, LLM client (configurable URL)
│   ├── graph/      # LangGraph workflows
│   ├── cards/      # paper cards, comparison tables
│   └── api/        # web API
├── eval/           # QASPER, ArxivDIGESTables, parser tests, my labels
├── notebooks/      # lessons + Colab benchmark notebooks
├── deploy/         # Dockerfiles, Kubernetes manifests
├── tests/
└── data/           # gitignored: downloaded papers, indexes
```

## 6. Build order

| Step | What | Main thing learned |
|---|---|---|
| 0 | Project skeleton ✅ | uv, git, GitHub |
| 1 | Tokens and transformers by hand: run a tiny model on the Mac | Tokenizers, logits, generation |
| 2 | Fetch one arXiv paper (HTML first, PDF fallback) and split it by section | Ingestion, parsing |
| 3 | Chunk, embed, vector search, without frameworks | Embeddings, similarity search |
| 4 | Answer with Llama 3.2 3B via a llama.cpp server, with citations | Serving, prompting, RAG end to end |
| 5 | Evaluation v1 on a QASPER subset (**v1 done**) | Retrieval and answer metrics |
| 6 | Improve retrieval: chunking, keyword + vector hybrid, reranker; measure each change | Experiments |
| 7 | PDF parser comparison, using arXiv HTML as the answer key | Parsing quality |
| 8 | Rebuild the pipeline with LangChain and compare to the hand-built one | LangChain |
| 9 | Paper card with structured JSON output (vLLM on Colab) | Constrained decoding |
| 10 | Serving benchmarks on Colab: transformers vs vLLM vs SGLang | Throughput, KV cache, prefix caching |
| 11 | LangGraph answer → verify → retry loop | LangGraph, state, loops |
| 12 | Multi-paper comparison table, scored on ArxivDIGESTables | Synthesis, evaluation |
| 13 | Related papers via the Semantic Scholar API and SPECTER2 | Paper-level retrieval |
| 14 | Docker: containerize the services | Images, containers |
| 15 | Kubernetes on a local cluster | Pods, services, jobs |
| 16 | Optional: fine-tune an embedding model | Training with transformers |
