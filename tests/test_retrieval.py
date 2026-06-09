from src.components.pdf_loader import PDFLoader
from src.components.chunker import Chunker
from src.components.embedder import Embedder
from src.components.vector_store import VectorStore
from src.components.retriever import Retriever

loader = PDFLoader()
chunker = Chunker()
embedder = Embedder()
vector_store = VectorStore()

text = loader.load_pdf(
    "data/raw/sample_ml_notes.pdf"
)

chunks = chunker.create_chunks(text)

embeddings = embedder.generate_embeddings(chunks)

index = vector_store.create_index(
    embeddings
)

retriever = Retriever(
    index=index,
    chunks=chunks,
    embedder=embedder
)

results = retriever.retrieve(
    "What is PCA?"
)

for i, result in enumerate(results):
    print(f"\nResult {i+1}")
    print(result)