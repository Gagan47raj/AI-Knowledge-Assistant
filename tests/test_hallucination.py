from app.services.hallucination_service import(HallucinationService)


def test_similarity_score():

    service = HallucinationService()

    score = service.evaluate(
        answer="FastAPI is a framework",
        context="FastAPI is a framework"
    )

    assert score > 0.80