
# 📄 Endee PDF RAG Chatbot

An AI-powered **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask natural language questions.  
The system retrieves the most relevant document chunks using **semantic vector search powered by Endee** and generates concise answers grounded in the uploaded document.


## 🚀 Project Overview

Large documents (research papers, reports, PDFs) are difficult to query efficiently.  
This project solves that problem by combining:

- **Semantic Search** using vector embeddings
- **Endee Vector Database** for similarity-based retrieval
- **RAG (Retrieval-Augmented Generation)** for accurate, context-aware answers
- **Streamlit UI** for an interactive user experience



## 🧠 Use Case Demonstrated

✅ Retrieval-Augmented Generation (RAG)  
✅ Semantic Search over PDFs  
✅ Practical AI application using vector databases


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

## 🧩 Project Structure
```
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

```
git clone <your-github-repo-url>
cd Endee-RAG-Chatbot
```

### 2️⃣ Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate   # Windows
```
### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
pip install streamlit sentence-transformers numpy pypdf transformers torch
```
### 4️⃣ Run the Application
```
streamlit run app.py
```
## 🧪 How to Use

- Upload a PDF document

- Click Process Document

- Ask any question related to the document

- The system retrieves relevant content and generates an answer

## 📸 Screenshots
<img width="1600" height="839" alt="image" src="https://github.com/user-attachments/assets/db79cb6d-d20a-43b4-a1ec-fcc6b6055fdf" />

  
PDF upload: <img width="1600" height="817" alt="image" src="https://github.com/user-attachments/assets/bcd84387-ca87-4acc-8fee-649d6e7622f8" />


Retrieved context: ![WhatsApp Image 2026-02-05 at 9 57 31 PM](https://github.com/user-attachments/assets/0e9b5c36-b5e2-4509-bc9d-f0bf9ad910d1)
![WhatsApp Image 2026-02-05 at 9 58 00 PM](https://github.com/user-attachments/assets/e01e092e-0fc5-4162-8402-2afa72e8b144)



Generated answer: ![WhatsApp Image 2026-02-05 at 9 58 26 PM](https://github.com/user-attachments/assets/f28c8de2-3c43-4007-a191-11935e9b04c4)



## 👩‍💻 Author

Deepika <br>
AI / ML Enthusiast
