from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(
    title="Interview Prep Assistant",
    description="RAG + Resume Parser + Mock Interview System",
    version="1.0.0"
)

app.include_router(router)