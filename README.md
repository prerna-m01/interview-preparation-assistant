# Interview Prep Assistant

An AI-powered Interview Preparation Assistant built using **FastAPI**, **RAG (Retrieval-Augmented Generation)**, **FAISS**, and **Google Gemini**.

---

## 🚀 Features

- PDF-based Knowledge Base  
- Semantic Search with FAISS  
- Retrieval-Augmented Generation (RAG)  
- Resume Parsing  
- Mock Interview Question Generation  
- Answer Evaluation & Feedback  
- Interview Report Generation  
- FastAPI Backend APIs  

---

## 🛠 Tech Stack

- Python  
- FastAPI  
- Google Gemini API  
- Sentence Transformers  
- FAISS  
- PyPDF  

---

## 🔄 Project Workflow

PDF → Chunking → Embeddings → FAISS → Retrieval → Gemini → Response Generation  

---

## 📦 Installation

### Clone the repository
```bash
git clone <repository-url>
cd interview-prep-assistant
```

### Create virtual environment
```bash
python -m venv venv
```

### Activate virtual environment

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

## 📚 API Documentation

```
http://127.0.0.1:8000/docs
```

---

## 🔌 Main Endpoints

- GET `/` → Home route  
- GET `/health` → Health check  
- GET `/ask?question=YOUR_QUESTION` → Ask interview questions  

---

## 🔮 Future Enhancements

- Resume-based interview generation  
- Authentication system  
- Docker deployment  
- PostgreSQL integration  
- Interview analytics dashboard  

---
