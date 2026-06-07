from app.services.intent_service import Intent_service

def test_weather_intent():

    service = Intent_service()

    intent = service.detect_intent(
        "What is weather in Bangalore?"
    )

    assert intent == "weather"