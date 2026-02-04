import json
import numpy as np
from backend.embeddings import generate_embedding

DATA_PATH = "data/embedded_vectors.json"


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def load_vectors():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def semantic_search(query, top_k=2):
    print("Performing semantic search...")

    query_vector = generate_embedding(query)

    vectors = load_vectors()

    scored_results = []

    for item in vectors:
        score = cosine_similarity(query_vector, item["vector"])

        scored_results.append({
            "score": float(score),
            "text": item["metadata"]["text"]
        })

    # Sort by similarity
    scored_results.sort(key=lambda x: x["score"], reverse=True)

    return scored_results[:top_k]
