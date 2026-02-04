# 📄 Endee PDF RAG Chatbot

An AI-powered **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask natural language questions.  
The system retrieves the most relevant document chunks using **semantic vector search powered by Endee** and generates concise answers grounded in the uploaded document.



## 🚀 Project Overview
```
Large documents (research papers, reports, PDFs) are difficult to query efficiently.  
This project solves that problem by combining:

- **Semantic Search** using vector embeddings
- **Endee Vector Database** for similarity-based retrieval
- **RAG (Retrieval-Augmented Generation)** for accurate, context-aware answers
- **Streamlit UI** for an interactive user experience

---

## 🧠 Use Case Demonstrated

✅ Retrieval-Augmented Generation (RAG)  
✅ Semantic Search over PDFs  
✅ Practical AI application using vector databases

---

## 🏗️ System Architecture

# 📄 Endee PDF RAG Chatbot

An AI-powered **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask natural language questions.  
The system retrieves the most relevant document chunks using **semantic vector search powered by Endee** and generates concise answers grounded in the uploaded document.

---

## 🚀 Project Overview

Large documents (research papers, reports, PDFs) are difficult to query efficiently.  
This project solves that problem by combining:

- **Semantic Search** using vector embeddings
- **Endee Vector Database** for similarity-based retrieval
- **RAG (Retrieval-Augmented Generation)** for accurate, context-aware answers
- **Streamlit UI** for an interactive user experience

---

## 🧠 Use Case Demonstrated

✅ Retrieval-Augmented Generation (RAG)  
✅ Semantic Search over PDFs  
✅ Practical AI application using vector databases

---

## 🏗️ System Architecture

User
↓
Streamlit UI (app.py)
↓
PDF Ingestion
→ Text Extraction
→ Chunking
→ Embedding Generation
↓
Vector Storage (Endee / JSON)
↓
Semantic Search (Cosine Similarity)
↓
Context Retrieval
↓
Answer Generation (LLM / HuggingFace)
```
## 🧩 Project Structure

Endee-RAG-Chatbot/
│
├── backend/
│ ├── ingestion/
│ │ ├── load_documents.py
│ │ └── load_pdf.py
│ │
│ ├── retrieval/
│ │ └── search_engine.py
│ │
│ ├── rag/
│ │ ├── answer_generator.py
│ │ └── qa_pipeline.py
│ │
│ ├── embeddings.py
│ ├── endee_client.py
│ └── config.py
│
├── data/
│ ├── embedded_vectors.json
│ ├── sample_docs.txt
│ └── sample.pdf
│
├── app.py
├── README.md
├── .gitignore
└── screenshots/
```
---

## 🗄️ How Endee Is Used

Endee is used as the **vector database** for semantic retrieval:

- Each document chunk is converted into a dense vector embedding
- Embeddings are stored as vectors
- User queries are embedded and compared using **cosine similarity**
- Top relevant chunks are retrieved and passed to the answer generator

This demonstrates **core vector search capabilities**, which are central to modern AI systems.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

````bash
git clone <your-github-repo-url>
cd Endee-RAG-Chatbot

### 2️⃣ Create Virtual Environment
``` bash

python -m venv venv
venv\Scripts\activate   # Windows
### 3️⃣ Install Dependencies
pip install -r requirements.txt
pip install streamlit sentence-transformers numpy pypdf transformers torch

### 4️⃣ Run the Application
streamlit run app.py

🧪 How to Use

Upload a PDF document

Click Process Document

Ask any question related to the document

The system retrieves relevant content and generates an answer

📸 Screenshots

Screenshots of:

PDF upload

Retrieved context

Generated answer

(Stored inside /screenshots folder)
👩‍💻 Author

Deepika
AI / ML Enthusiast
````
