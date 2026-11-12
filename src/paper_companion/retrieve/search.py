"""Find the chunks closest in meaning to a question."""

from paper_companion.index.vectors import QUERY_PREFIX, get_model


def search(query, chunks, vectors, k=3):
    q = get_model().encode(QUERY_PREFIX + query, normalize_embeddings=True)
    scores = vectors @ q
    top = scores.argsort()[::-1][:k]
    return [{**chunks[i], "score": float(scores[i])} for i in top]