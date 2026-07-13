# VeriRAG: Self-Correcting RAG Pipeline

## Overview

VeriRAG is an intelligent Retrieval-Augmented Generation (RAG) system designed to reduce AI hallucinations by validating retrieved information before generating responses.

Unlike traditional RAG pipelines, VeriRAG introduces a Self-Correction Engine that detects insufficient or conflicting context, automatically rewrites queries, performs re-retrieval, or requests user clarification before generating the final response.

---

## Problem Statement

Traditional RAG systems may hallucinate when:

- Retrieved context is insufficient
- Documents contain conflicting information
- User queries are ambiguous

VeriRAG addresses these challenges by introducing a validation and self-correction layer.

---

## Features

- Semantic document retrieval
- Context validation
- Confidence scoring
- Conflict detection
- Query rewriting
- Automatic re-retrieval
- User clarification
- Grounded response generation
- Monitoring Dashboard
- Hallucination tracking
- Alerting & Escalation

---

## Architecture

User
↓

Query Processor

↓

Embedding Model

↓

Qdrant Vector Database

↓

Context Evaluation

↓

Self-Correction Engine

↓

LLM

↓

Verified Response

↓

Monitoring Dashboard

---

## Technology Stack

- Python
- FastAPI
- Mastra
- Qdrant
- OpenAI / Llama 3
- LangChain
- Docker

---

## Folder Structure
VeriRAG/
│
├── docs/
│ ├── PRD.pdf
│ ├── Architecture.png
│ └── SolutionOverview.md
│
├── backend/
│ ├── api.py
│ ├── retriever.py
│ ├── validator.py
│ ├── self_correct.py
│ ├── generator.py
│ └── monitor.py
│
├── frontend/
│
├── data/
│
├── evaluation/
│
├── tests/
│
├── requirements.txt
│
└── README.md



---

## Workflow

1. Receive user query
2. Generate embeddings
3. Retrieve documents from Qdrant
4. Validate retrieved context
5. Detect conflicts
6. Rewrite query if needed
7. Re-retrieve documents
8. Generate grounded response
9. Monitor performance
10. Display analytics

---

## KPIs

- Hallucination Rate
- Retrieval Accuracy
- Confidence Score
- Response Time
- User Satisfaction
- Re-query Count

---

## Future Work

- Multimodal RAG
- Voice Support
- Fine-tuned Query Rewriter
- Continuous Learning
- Human-in-the-loop Validation

---

## Contributors

Nushra Fathima

