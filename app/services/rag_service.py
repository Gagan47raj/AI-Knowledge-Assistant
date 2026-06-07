from app.services.retrieval_service import RetrievalService
from app.services.prompt_service import PromptService
from app.services.mistral_service import MistralService
from app.utils.logger import logger

from app.services.hallucination_service import (HallucinationService)



class RAGService:

    def __init__(self):

        self.retrieval_service = RetrievalService()
        self.prompt_service = PromptService()
        self.mistral_service = MistralService()
        self.hallucination_service = (HallucinationService())

    def ask(
        self,
        question,
        request_id=None
    ):
        
        results = (
            self.retrieval_service.retrieve(question)
        )

        logger.info(
           f"Question: {question}"
        )

        context = "\n".join(
            results["documents"][0]
        )

        prompt = (
            self.prompt_service.build_prompt(
                question,
                context
            )
        )

        logger.info(
            "Context retrieved successfully"
        )

        try:
            answer = (
                self.mistral_service.generate_response(prompt)
            )

            logger.info(
                "Answer generated"
            )

        except Exception as e:
            logger.error(str(e))

            raise Exception("Model Offline")
        

        similarity = (
             self.hallucination_service.evaluate(answer, context)
        )

        confidence = (
             self.hallucination_service.confidence_score(similarity)
        )   

        risk = (
            self.hallucination_service.get_risk_level(similarity)
        )

        logger.info(
            f"Confidence: {confidence}"
        )

        logger.info(
            f"Risk: {risk}"
        )

        return {
            "question": question,
            "context": context,
            "answer": answer,
            "confidence" : confidence,
            "hallucination_risk" : risk
        }