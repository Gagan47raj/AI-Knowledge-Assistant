class Intent_service:

    def detect_intent(self, question:str):
        question = question.lower()

        if "weather" in question:
            return "weather"
        
        if "time" in question:
            return "Time"
        
        if question in [
            "hi",
            "hello",
            "hey",
            "how are you"
        ]: return "greeting"
        
        return "knowledge"