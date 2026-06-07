from ollama import chat

reponse = chat(
    model = "mistral",
    messages=[
        {
            "role": "user",
            "content": "Hello"
        }
    ]
)

print(reponse["message"]["content"])