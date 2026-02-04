import os
import json
from backend.embeddings import generate_embedding

DATA_PATH = "data/sample_docs.txt"
OUTPUT_PATH = "data/embedded_vectors.json"


def load_documents():
    print("Loading documents...")

    if not os.path.exists(DATA_PATH):
        print("Data file not found")
        return

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = [c.strip() for c in text.split("\n") if c.strip()]

    print(f"Found {len(chunks)} chunks")

    vectors = []

    for idx, chunk in enumerate(chunks):
        embedding = generate_embedding(chunk)

        vectors.append({
            "id": f"doc_{idx}",
            "vector": embedding,
            "metadata": {
                "text": chunk
            }
        })

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(vectors, f, indent=2)

    print("Saved embeddings to:", OUTPUT_PATH)


if __name__ == "__main__":
    load_documents()
