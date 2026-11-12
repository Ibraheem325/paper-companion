"""Chunk a paper, embed the chunks with bge-small, and save/load the index."""

import json
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "BAAI/bge-small-en-v1.5"
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "
INDEX_DIR = Path(__file__).resolve().parents[3] / "data" / "index"

_model = None


def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model


def chunk_words(text, size=200, overlap=40):
    words = text.split()
    step = size - overlap
    return [" ".join(words[i:i + size]) for i in range(0, max(len(words) - overlap, 1), step)]


def chunk_paper(paper, size=200, overlap=40):
    chunks = []
    for s in paper["sections"]:
        for i, c in enumerate(chunk_words(s["text"], size, overlap)):
            chunks.append({"arxiv_id": paper["arxiv_id"], "section": s["title"], "chunk": i, "text": c})
    return chunks


def build_index(paper):
    chunks = chunk_paper(paper)
    vectors = get_model().encode([c["text"] for c in chunks], normalize_embeddings=True)
    return chunks, vectors


def save_index(arxiv_id, chunks, vectors):
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    np.save(INDEX_DIR / f"{arxiv_id}.npy", vectors)
    (INDEX_DIR / f"{arxiv_id}.json").write_text(json.dumps(chunks, ensure_ascii=False))


def load_index(arxiv_id):
    vectors = np.load(INDEX_DIR / f"{arxiv_id}.npy")
    chunks = json.loads((INDEX_DIR / f"{arxiv_id}.json").read_text())
    return chunks, vectors