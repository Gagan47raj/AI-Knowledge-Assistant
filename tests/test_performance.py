import time

from app.services.rag_service import RAGService

rag = RAGService()
start = time.time()

response = rag.ask(
    "What is FastAPI?"
)

end = time.time()

execution_time = end - start

assert execution_time < 10