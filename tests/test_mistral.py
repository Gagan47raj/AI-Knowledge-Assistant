from app.services.mistral_service import MistralService

mistral = MistralService()

response = mistral.generate_response(
    "What is machine learning?"
)

print(response)