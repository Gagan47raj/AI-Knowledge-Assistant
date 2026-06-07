from app.services.embedding_service import (
    EmbeddingService
)

def test_embedding_generation():

    service = EmbeddingService()

    vector = service.generate_embedding(
        "Machine Learning"
    )

    assert isinstance(vector, list)

    assert len(vector) == 384