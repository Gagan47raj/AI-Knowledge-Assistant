from sklearn.metrics.pairwise import cosine_similarity

from app.services.embedding_service import (EmbeddingService)

class HallucinationService:
    
    def __init__(self):
        self.embedding_service = (EmbeddingService())

    def evaluate(self, answer : str, context : str):

        answer_embedding = (
            self.embedding_service.generate_embedding(answer)
        )

        context_embedding = (
            self.embedding_service.generate_embedding(context)
        )

        similarity = cosine_similarity(
            [answer_embedding],
            [context_embedding]
        )[0][0]

        return similarity
    
    def get_risk_level(self, similarity):
        if similarity >= 0.8:
            return "low"
        elif similarity >= 0.6:
            return "Medium"
        
        return "High"
    
    def confidence_score(self, similarity):
        return round(similarity * 100, 2)