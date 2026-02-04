import json
from pypdf import PdfReader
from backend.embeddings import generate_embedding

OUTPUT_PATH = "data/embedded_vectors.json"


def extract_text_from_pdf_file(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def chunk_text(text, chunk_size=300):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


def process_uploaded_pdf(uploaded_file):
    print("Processing uploaded PDF...")

    text = extract_text_from_pdf_file(uploaded_file)

    chunks = chunk_text(text)

    vectors = []

    for i, chunk in enumerate(chunks):
        embedding = generate_embedding(chunk)

        vectors.append({
            "id": f"pdf_{i}",
            "vector": embedding,
            "metadata": {
                "text": chunk
            }
        })

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(vectors, f, indent=2)

    return len(chunks)
