from pydantic import BaseModel

class QuestionResponse(BaseModel):

    request_id: str

    question: str

    answer: str

    confidence: float

    hallucination_risk: str

    sources: list

    execution_time: float