from app.services.intent_service import (
    Intent_service
)

from app.services.function_service import (
    FunctionService
)

from app.services.weather_service import (
    WeatherService
)

from app.services.rag_service import (
    RAGService
)

class AgentService:

    def __init__(self):
        
        self.intent_service = Intent_service()
        self.function_service = FunctionService()
        self.weather_service = WeatherService()
        self.rag_service = RAGService()

    def process(self, question, request_id):

        intent = (self.intent_service.detect_intent(question))
        if intent == "weather":
            return {
                "intent" : "weather",
                "result" : self.weather_service.get_weather()
            }
        
        if intent == "time":
            return {
                "intent" : "time",
                "result" : self.function_service.get_current_time()
            }
        
        if intent == "greeting":
            return {
                "intent" : "greeting",
                "result" : "Hello! How can I help you?"
            }
        
        return self.rag_service.ask(question, request_id)