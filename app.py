from fastapi import FastAPI
from pydantic import BaseModel

from retriever import retrieve_documents
from validator import validate_context
from self_correct import rewrite_query
from generator import generate_answer

app = FastAPI(title="VeriRAG")

class Query(BaseModel):
    question: str

@app.post("/chat")
def chat(query: Query):

    docs = retrieve_documents(query.question)

    confidence = validate_context(query.question, docs)

    if confidence < 0.75:
        improved_query = rewrite_query(query.question)
        docs = retrieve_documents(improved_query)

    answer = generate_answer(query.question, docs)

    return {
        "question": query.question,
        "confidence": confidence,
        "documents": docs,
        "answer": answer
    }