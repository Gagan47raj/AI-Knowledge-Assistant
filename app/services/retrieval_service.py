from app.services.embedding_service import EmbeddingService
from app.services.chroma_service import ChromaService

class RetrievalService:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.chroma_service = ChromaService()

    def retrieve(
            self,
            query,
            top_k=3
    ):
        
        query_embedding = (
            self.embedding_service.generate_embedding(query)
        )

        results = (
            self.chroma_service.search(
                query_embedding,
                top_k
            )
        )

        return results