from app.services.retrieval_service import RetrievalService

def test_retrieval():

    service = RetrievalService()

    results = service.retrieve(
        "What is AI?"
    )

    assert len(
        results["documents"][0]
    ) > 0