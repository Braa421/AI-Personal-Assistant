from rag.embeddings import embed_text
from rag.vector_store import load_vectors
import math

def cosine_similarity(vector1: list[float], vector2: list[float])-> float:
    dot_product = 0
    magnitude1 = 0
    magnitude2 = 0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
    for value in vector1:
        magnitude1 += value ** 2
    magnitude1 = math.sqrt(magnitude1)
    for value in vector2:
        magnitude2 += value ** 2
    magnitude2 = math.sqrt(magnitude2)
    denominator = magnitude1 * magnitude2
    if denominator == 0:
        return 0.0
    return dot_product/denominator
def retrieve(query: str, top_k: int = 3)-> list[dict]:
    query_vector = embed_text(query)
    store = load_vectors()
    results = []
    for item in store:
        score = cosine_similarity(query_vector, item["vector"])
        results.append(
            {
                "text": item["text"],
                "score": score
            }
        )
    results.sort(key = lambda item: item["score"], reverse = True)
    return results[:top_k]