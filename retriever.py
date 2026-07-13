from qdrant_client import QdrantClient

client = QdrantClient(
    url="http://localhost:6333"
)

COLLECTION = "knowledge_base"

def retrieve_documents(query):

    # Placeholder retrieval
    return [
        "Document 1 about AI",
        "Document 2 about RAG",
        "Document 3 about Self Correction"
    ]