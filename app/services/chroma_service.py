import chromadb

class ChromaService:
    def __init__(self):
        self.client = chromadb.PersistentClient(
            path="./data/chroma"
        )

        self.collection = self.client.get_or_create_collection(
            name="knowledge_base"
        )

    def add_documents(
            self,
            doc_id,
            document,
            embedding
    ):
        self.collection.add(
            ids=[doc_id],
            documents=[document],
            embeddings=[embedding]
        )
    
    def search(
            self,
            query_embeddings,
            n_results=3
    ):
        results = self.collection.query(
            query_embeddings=[query_embeddings],
            n_results=n_results
        )

        return results