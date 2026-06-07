class PromptService:

    def build_prompt(
        self,
        question,
        context
    ):

        prompt = f"""
You are an AI Knowledge Assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
reply:

"I could not find this information in the knowledge base."

Context:
{context}

Question:
{question}

Answer:
"""

        return prompt