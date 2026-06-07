from app.services.embedding_service import EmbeddingService
from app.services.chroma_service import ChromaService
from app.services.document_loader import DocumentLoader

embedding_service = EmbeddingService()
chroma_service = ChromaService()
loader = DocumentLoader()

documents = loader.load_documents()

for idx, document in enumerate(documents):

    embedding = embedding_service.generate_embedding(
        document
    )

    chroma_service.add_documents(
        doc_id=str(idx),
        document=document,
        embedding=embedding
    )

print("Documents indexed successfully")

