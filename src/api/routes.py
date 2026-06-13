from fastapi import APIRouter, UploadFile, File
import os

from src.utils import extract_score

from src.components.pdf_loader import PDFLoader
from src.components.chunker import Chunker
from src.components.embedder import Embedder
from src.components.vector_store import VectorStore
from src.components.retriever import Retriever
from src.pipeline.rag_pipeline import RAGPipeline
from src.components.evaluator import Evaluator

from src.database.session import SessionLocal
from src.repositories.interview_repository import InterviewRepository
from src.components.weak_topic_extractor import WeakTopicExtractor

router = APIRouter()

# INITIALIZE COMPONENTS

# INITIALIZE COMPONENTS

print("ROUTES 1")
loader = PDFLoader()

print("ROUTES 2")
chunker = Chunker()

print("ROUTES 3")
embedder = Embedder()

print("ROUTES 4")
vector_store = VectorStore()

print("ROUTES 5")
evaluator = Evaluator()

print("ROUTES 6")
repository = InterviewRepository()

print("ROUTES 7")
weak_topic_extractor = WeakTopicExtractor()

print("ROUTES 8")

INDEX_PATH = "vectorstore/index.faiss"
CHUNKS_PATH = "vectorstore/chunks.pkl"

print("INDEX EXISTS:", os.path.exists(INDEX_PATH))
print("CHUNKS EXISTS:", os.path.exists(CHUNKS_PATH))

# LOAD OR CREATE VECTORSTORE

print("ROUTES 9")

if os.path.exists(INDEX_PATH) and os.path.exists(CHUNKS_PATH):

    print("ROUTES 10 - Loading existing FAISS")

    index = vector_store.load_index(INDEX_PATH)

    print("ROUTES 11")

    chunks = vector_store.load_chunks(CHUNKS_PATH)

    print("ROUTES 12")

else:

    print("ROUTES 13 - Building new FAISS")

    text = loader.load_pdf(
        "data/raw/sample_ml_notes.pdf"
    )

    print("ROUTES 14")

    chunks = chunker.create_chunks(text)

    print("ROUTES 15")

    embeddings = embedder.generate_embeddings(chunks)

    print("ROUTES 16")

    index = vector_store.create_index(embeddings)

    print("ROUTES 17")

    vector_store.save_index(
        index,
        INDEX_PATH
    )

    vector_store.save_chunks(
        chunks,
        CHUNKS_PATH
    )

retriever = Retriever(
    index=index,
    chunks=chunks,
    embedder=embedder
)

rag = RAGPipeline(retriever)

# ROUTES

@router.get("/")
def home():

    return {
        "message": "API Running"
    }


# 1. ASK QUESTION (RAG)

@router.post("/ask")
def ask(question: str):

    answer = rag.answer_question(
        question
    )

    return {
        "question": question,
        "answer": answer
    }


# 2. START INTERVIEW

@router.post("/start-interview")
def start_interview(
    topic: str,
    num_questions: int = 3
):

    return {
        "topic": topic,
        "questions": [
            f"What is {topic}?",
            f"Explain applications of {topic}?",
            f"What are challenges in {topic}?"
        ]
    }


# 3. EVALUATE ANSWER

@router.post("/evaluate-answer")
def evaluate_answer(
    question: str,
    candidate_answer: str
):

    result = evaluator.evaluate_answer(
        question,
        candidate_answer
    )

    score = extract_score(result)
    weak_topics = weak_topic_extractor.extract(result)

    db = SessionLocal()

    try:

        repository.save(
            db=db,
            question=question,
            candidate_answer=candidate_answer,
            evaluation=result,
            score=score,
            weak_topics=weak_topics
        )

    finally:

        db.close()

    return {
        "evaluation": result,
        "score": score
    }


# 4. UPLOAD RESUME

@router.post("/upload-resume")
def upload_resume(
    file: UploadFile = File(...)
):

    content = file.file.read()

    return {
        "filename": file.filename,
        "message": "Resume received successfully",
        "size": len(content)
    }


# 5. INTERVIEW HISTORY

@router.get("/history")
def history():

    db = SessionLocal()

    try:

        records = repository.get_all(
            db
        )

        return {
            "history": [
                {
                    "id": record.id,
                    "question": record.question,
                    "answer": record.candidate_answer,
                    "evaluation": record.evaluation,
                    "score": record.score,
                    "weak_topics": record.weak_topics
                }
                for record in records
            ]
        }
    

    finally:

        db.close()

@router.get("/analytics")
def analytics():

    db = SessionLocal()

    try:

        total_interviews = repository.get_total_interviews(db)

        average_score = repository.get_average_score(db)

        highest_score = repository.get_highest_score(db)

        lowest_score = repository.get_lowest_score(db)

        return {
            "total_interviews": total_interviews,
            "average_score": round(average_score, 2)
            if average_score else 0,

            "highest_score": highest_score
            if highest_score else 0,

            "lowest_score": lowest_score
            if lowest_score else 0
        }

    finally:

        db.close()

@router.get("/weak-topics")
def weak_topics():

    db = SessionLocal()

    try:

        topics = repository.get_common_weak_topics(
            db
        )

        return {
            "common_weak_topics": topics
        }

    finally:

        db.close()