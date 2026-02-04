import streamlit as st
from backend.ingestion.load_pdf import process_uploaded_pdf
from backend.retrieval.search_engine import semantic_search
from backend.rag.answer_generator import generate_answer

st.set_page_config(page_title="Endee RAG PDF Chatbot")

st.title("Endee PDF RAG Chatbot")
st.write("Upload a PDF and ask questions using semantic search + AI")

# ---------------- PDF Upload ----------------

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    if st.button("Process Document"):
        with st.spinner("Processing PDF and generating embeddings..."):
            chunks = process_uploaded_pdf(uploaded_file)

        st.success(f"Document processed successfully! {chunks} chunks created.")

st.divider()

# ---------------- Question Input ----------------

query = st.text_input("Ask a question about the document")

if st.button("Ask"):

    if query.strip() == "":
        st.warning("Please enter a question")

    else:
        with st.spinner("Searching relevant context..."):
            results = semantic_search(query, top_k=2)

        st.subheader("Retrieved Context")

        for item in results:
            st.write(f"Similarity Score: {round(item['score'], 3)}")
            st.write(item["text"])
            st.write("------")

        st.subheader("Answer")

        with st.spinner("Generating AI answer..."):
            final_answer = generate_answer(query, results)

        st.success(final_answer)
