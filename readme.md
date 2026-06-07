# 📄 AI Knowledge Assistant

An enterprise-grade Document Intelligence and Retrieval-Augmented Generation (RAG) system built with Python, FastAPI, Ollama, Mistral, ChromaDB, Sentence Transformers, and Streamlit.

The application enables users to upload documents (PDF, DOCX, TXT), perform semantic search, retrieve relevant information using vector embeddings, and interact with their documents through natural language queries.

---

# Key Capabilities

## Document Processing
- Support for PDF, DOCX, and TXT formats
- Automated text extraction and cleaning
- Intelligent document chunking with configurable overlap
- Metadata preservation for source tracking

## Retrieval-Augmented Generation (RAG)
- Semantic search using high-quality embeddings
- Vector storage and retrieval via ChromaDB
- Similarity-based context selection
- Grounded answer generation using retrieved document chunks

## AI Engineering Features
- Intent classification and routing
- Function calling for structured actions
- Hallucination risk evaluation
- Confidence scoring and calibration
- Structured JSON responses with citations
- Source attribution for traceability

## Backend Engineering Features
- RESTful APIs built with FastAPI
- Dependency injection for testability
- Structured logging with request tracking
- Centralized exception handling
- Health check and readiness probes
- API versioning (`/api/v1/*`)
- Request ID propagation across services

---

# System Architecture

```text
                 User
                  │
                  ▼
            Streamlit UI
                  │
                  ▼
              FastAPI
                  │
                  ▼
           Agent Service
                  │
      ┌───────────┴───────────┐
      │                       │
      ▼                       ▼
  Function Calls         RAG Pipeline
      │                       │
      ▼                       ▼
 External APIs         ChromaDB Vector Store
                              │
                              ▼
                      Semantic Retrieval
                              │
                              ▼
                         Ollama + Mistral
                              │
                              ▼
                    Hallucination Detection
                              │
                              ▼
                        Final Response
```

---

# Project Structure

```text
AI-Knowledge-Assistant/
│
├── app/
│   ├── api/               # Route handlers and endpoints
│   ├── core/              # Configuration, dependencies, security
│   ├── models/            # Pydantic schemas and domain models
│   ├── services/          # Business logic: RAG, embedding, LLM
│   ├── utils/             # Helpers: chunking, text extraction
│   └── main.py            # FastAPI application entry point
│
├── data/
│   ├── uploads/           # Temporary file storage
│   └── chroma/            # Persistent vector database
│
├── docs/                  # Additional documentation
├── tests/                 # Unit and integration tests
├── logs/                  # Application logs
│
├── streamlit_app.py       # Streamlit frontend
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
├── Dockerfile             # Container configuration
├── .gitignore
└── README.md
```

---

# Technology Stack

| Category             | Technology                          |
|----------------------|-------------------------------------|
| Language             | Python 3.10+                        |
| Backend Framework    | FastAPI                             |
| Frontend             | Streamlit                           |
| LLM                  | Mistral (7B) via Ollama             |
| LLM Runtime          | Ollama                              |
| Vector Database      | ChromaDB (Persistent)               |
| Embedding Model      | Sentence Transformers (all-MiniLM-L6-v2) |
| API Documentation    | Swagger UI / OpenAPI (auto-generated) |
| Testing              | Pytest, pytest-cov                  |
| Containerization     | Docker                              |

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-knowledge-assistant.git
cd ai-knowledge-assistant
```

## 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
# or
venv\Scripts\activate         # Windows
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Install and Configure Ollama

Download and install Ollama from [ollama.com](https://ollama.com). Then pull the Mistral model:

```bash
ollama pull mistral
```

Verify the installation:

```bash
ollama run mistral
```

## 5. Environment Configuration

```bash
cp .env.example .env
# Edit .env with your preferred settings
```

---

# Running the Application

## Start FastAPI Backend (Development)

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- Backend URL: `http://localhost:8000`
- Swagger Documentation: `http://localhost:8000/docs`

## Start Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

- Frontend URL: `http://localhost:8501`

---

# Usage Guide

1. **Upload a Document**  
   Supported formats: PDF, DOCX, TXT

2. **Document Processing Pipeline**  
   - Text extraction  
   - Document chunking  
   - Embedding generation  
   - Vector storage in ChromaDB

3. **Ask Questions**  
   Example queries:
   - "What are the key learning outcomes?"
   - "Summarize the section on transformer architectures."
   - "List all references cited in this document."

4. **Receive Grounded Responses**  
   Each answer includes confidence scores, source citations, and hallucination risk assessment.

---

# API Endpoints

## Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

## Ask Question

```http
POST /api/v1/ask
Content-Type: application/json
```

Request Body:

```json
{
  "question": "What is FastAPI?",
  "session_id": "optional-uuid"
}
```

Response:

```json
{
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "question": "What is FastAPI?",
  "answer": "FastAPI is a modern web framework for building APIs with Python, based on standard Python type hints.",
  "confidence": 92.4,
  "hallucination_risk": "low",
  "sources": [
    {
      "filename": "fastapi_docs.pdf",
      "chunk_id": 3,
      "similarity_score": 0.87
    }
  ],
  "execution_time_ms": 720
}
```

## Upload Document

```http
POST /api/v1/documents/upload
Content-Type: multipart/form-data
```

Response:

```json
{
  "document_id": "doc_123",
  "filename": "example.pdf",
  "status": "processed",
  "chunk_count": 24
}
```

---

# Testing

Run all tests with coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

Expected minimum coverage: 80%

Run specific test suite:

```bash
pytest tests/test_rag_pipeline.py -v
```

---

# Security Considerations

- Input validation using Pydantic models
- Exception handling without information leakage
- Environment-based configuration (no hardcoded secrets)
- Request logging for auditability
- Health monitoring for operational visibility
- Structured responses to prevent injection attacks

---

# Cost Structure

This system is designed for local execution with zero recurring costs.

| Component               | Cost Model        |
|-------------------------|-------------------|
| Ollama + Mistral        | Free (local)      |
| FastAPI + Streamlit     | Free (open source)|
| ChromaDB                | Free (embedded)   |
| Sentence Transformers   | Free (MIT license)|

Estimated monthly operational cost for development: **$0**

For production deployment, cloud hosting costs apply (e.g., AWS, GCP, Azure).

---

# Future Enhancements

- Multi-document conversation with session memory
- Conversational agents with LangGraph
- User authentication and role-based access control
- Hybrid search (dense + sparse retrieval)
- Redis-based response caching
- PostgreSQL for metadata and conversation history
- Support for image and spreadsheet documents
- Deployment templates for AWS ECS / Kubernetes

---

# Author

**Gagan**  
AI Knowledge Assistant – Capstone Project  
Built on Retrieval-Augmented Generation (RAG) architecture with local-first design principles.

---

# License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

# Contributing

Issues and pull requests are welcome. For major changes, please open an issue first to discuss the proposed changes.

---

**If you find this project useful, please consider starring the repository and sharing your feedback.**
