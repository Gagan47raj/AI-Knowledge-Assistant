from app.services.rag_service import RAGService

def test_rag_pipeline():

    rag = RAGService()

    response = rag.ask(
        "What is FastAPI?"
    )

    assert "answer" in response