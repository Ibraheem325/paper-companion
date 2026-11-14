"""Answer a question about a paper with the local LLM, citing sections."""

import os
import re

import httpx

from paper_companion.index.vectors import load_index
from paper_companion.retrieve.search import search

LLM_URL = os.environ.get("LLM_URL", "http://127.0.0.1:8080/v1/chat/completions")

SYSTEM = (
    "Answer only from the context. After each fact, cite its section in brackets, "
    "like [Abstract]. If the context does not contain the answer, say you do not know."
)

FORMAT_RULE = (
    "End every sentence with its section in brackets, copied exactly from the context, "
    "for example: The dataset contains 500 images [2 Data Collection]. "
    "If the context does not contain the answer, reply only: I do not know."
)


def build_messages(question, hits):
    context = "\n\n".join(f"[{h['section']}] {h['text']}" for h in hits)
    user = f"Context:\n{context}\n\nQuestion: {question}\n\n{FORMAT_RULE}"
    return [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": user},
    ]


def plain_math(text):
    """Turn inline LaTeX like $N=6$ into N = 6."""
    return re.sub(r"\$([^$]+)\$", lambda m: re.sub(r"\s*=\s*", " = ", m.group(1)), text)


def answer(question, arxiv_id, k=3):
    chunks, vectors = load_index(arxiv_id)
    hits = search(question, chunks, vectors, k=k)
    response = httpx.post(LLM_URL, json={"messages": build_messages(question, hits)}, timeout=60)
    response.raise_for_status()
    return plain_math(response.json()["choices"][0]["message"]["content"]), hits