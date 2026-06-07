from fastapi import APIRouter
from app.services.rag_service import RAGService
from app.models.request import (
    QuestionRequest
)

from app.services.agent_service import (
    AgentService
)

from fastapi import Depends

from app.core.dependencies import (
    get_agent_service
)

from app.utils.request_tracker import (
    generate_request_id
)

router = APIRouter()

rag_service = RAGService()
agent_service = AgentService()

@router.get("/ask")
def ask(
    question: str,
    agent_service: AgentService = Depends(get_agent_service)
):

    request_id = generate_request_id()

    response = agent_service.process(
        question,
        request_id=request_id
    )

    return {
        "request_id": request_id,
        "response": response
    }
