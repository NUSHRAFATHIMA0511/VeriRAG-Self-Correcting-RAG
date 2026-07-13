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
