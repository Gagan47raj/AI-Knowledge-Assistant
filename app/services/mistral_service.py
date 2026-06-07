from ollama import chat

class MistralService:

    def generate_response(self, prompt: str):

        response = chat(
            model = "mistral",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]