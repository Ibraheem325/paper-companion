# Allowed sources

Official sites the harness may read to explain or verify a technology. My
design doc and code always win over these. Prefer the official docs; use
GitHub READMEs, papers or model/dataset cards only when the docs don't cover it.

## Technologies

| Technology | Official docs | Used in steps |
|---|---|---|
| uv | https://docs.astral.sh/uv/ | 0 |
| Hugging Face transformers | https://huggingface.co/docs/transformers | 1, 3, 6, 10, 16 |
| Hugging Face datasets | https://huggingface.co/docs/datasets | 5, 12 |
| Sentence Transformers (embeddings, rerankers) | https://sbert.net | 3, 6, 16 |
| llama.cpp | https://github.com/ggml-org/llama.cpp (README and `docs/`) | 4 |
| Llama 3.2 3B model card | https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct | 4 |
| vLLM | https://docs.vllm.ai | 9, 10 |
| SGLang | https://docs.sglang.io | 10 |
| LangChain and LangGraph | https://docs.langchain.com | 8, 11 |
| Docker | https://docs.docker.com | 14 |
| Kubernetes | https://kubernetes.io/docs/ | 15 |
| Google Colab FAQ | https://research.google.com/colaboratory/faq.html | 9, 10 |

## Papers, data and APIs

| Source | Link | Used in steps |
|---|---|---|
| arXiv API | https://info.arxiv.org/help/api/ | 2 |
| QASPER dataset | https://huggingface.co/datasets/allenai/qasper | 5 |
| ArxivDIGESTables paper | https://arxiv.org/abs/2410.22360 | 12 |
| ArxivDIGESTables data | https://huggingface.co/datasets/blnewman/arxivDIGESTables | 12 |
| Semantic Scholar API | https://api.semanticscholar.org/api-docs/ | 13 |
| SPECTER2 model card | https://huggingface.co/allenai/specter2 | 13 |
