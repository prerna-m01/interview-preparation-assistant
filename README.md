# Interview Prep Assistant

An AI-powered Interview Preparation Assistant built using **FastAPI**, **RAG (Retrieval-Augmented Generation)**, **FAISS**, and **Google Gemini**.  

The system helps users prepare for interviews through document-based question answering, mock interviews, resume analysis, and automated answer evaluation.

---

## 🚀 Features

- 📄 PDF Knowledge Base Processing  
- 🔍 Semantic Search using FAISS  
- 🤖 RAG-based Question Answering System  
- 📑 Resume Parsing and Analysis  
- 🎯 Mock Interview Question Generation  
- 📝 AI-powered Answer Evaluation  
- 📊 Interview Report Generation  
- 📚 Interview History Tracking  
- 🚀 FastAPI Backend with Swagger Documentation  

---

## 🛠 Tech Stack

- Python  
- FastAPI  
- Google Gemini API  
- Sentence Transformers  
- FAISS  
- PyPDF  
- Uvicorn  

---

## 📁 Project Structure


```
interview-prep-assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── data/
│   ├── raw/
│   └── interviews/
│
├── vectorstore/
│   ├── index.faiss
│   └── chunks.pkl
│
├── src/
│   ├── api/
│   │   └── routes.py
│   │
│   ├── components/
│   │   ├── pdf_loader.py
│   │   ├── chunker.py
│   │   ├── embedder.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   ├── llm_client.py
│   │   ├── question_generator.py
│   │   ├── evaluator.py
│   │   ├── resume_parser.py
│   │   └── report_generator.py
│   │
│   └── pipeline/
│       ├── rag_pipeline.py
│       └── interview_pipeline.py
│
├── tests/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── test_evaluator.py
│   ├── test_history.py
│   ├── test_interview.py
│   ├── test_llm.py
│   ├── test_question_generator.py
│   ├── test_rag.py
│   ├── test_resume_parser.py
│   └── test_retrieval.py
│
└── README.md
```

## ⚙️ Installation

### Clone the repository
```bash
git clone <repository-url>
cd interview-prep-assistant
```

### Create virtual environment
```bash
python -m venv venv
```

### Activate environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key
```

---

## ▶️ Run the Application

```bash
uvicorn app:app --reload
```

---

## 🌐 Server Access

- **Base URL:** http://127.0.0.1:8000  
- **Swagger Docs:** http://127.0.0.1:8000/docs  

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home endpoint |
| POST | `/ask` | Ask questions from knowledge base |
| POST | `/start-interview` | Generate interview questions |
| POST | `/evaluate-answer` | Evaluate candidate answers |
| POST | `/upload-resume` | Parse resume |
| GET | `/history` | View interview history |

---

## 🔄 Workflow

```
PDF Documents
      ↓
Text Chunking
      ↓
Embeddings Generation
      ↓
FAISS Vector Store
      ↓
Retriever
      ↓
Google Gemini LLM
      ↓
Final Generated Response
```

---

## 🔮 Future Enhancements

- User Authentication System  
- PostgreSQL Database Integration  
- Docker Deployment  
- Resume-based Personalized Interviews  
- Performance Analytics Dashboard  
- Voice-based Mock Interviews  

---