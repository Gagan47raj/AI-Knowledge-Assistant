class ChunkingService:

    def chunk_text(
        self,
        text,
        chunk_size=500,
        overlap=100
    ):

        chunks = []

        step = chunk_size - overlap

        for i in range(
            0,
            len(text),
            step
        ):

            chunks.append(
                text[i:i + chunk_size]
            )

        return chunks