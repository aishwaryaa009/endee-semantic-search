# Semantic Search System using Endee Vector Database

## Overview

This project demonstrates a **Semantic Search system** built using  
**transformer-based embeddings** and **Endee**, a high-performance open-source  
vector database.

The project focuses on **vector search architecture, system integration, and  
deployment**, rather than UI-level presentation.

---

## Use Case: Semantic Search

Semantic search retrieves results based on **meaning**, not just keywords.

### Example

- **Query:** “What is a vector database?”
- **Relevant Result:** “Vector databases store embeddings for similarity search.”

This system converts text into embeddings and uses a vector database to support  
similarity-based retrieval.

---

## Architecture

User Query  
↓  
Sentence Transformer Model  
↓  
Vector Embedding  
↓  
Endee Vector Database  
↓  
Similarity-based Results  

---

## Technologies Used

- Python 3.11  
- Sentence Transformers (`all-MiniLM-L6-v2`)  
- Endee Vector Database  
- Docker  
- REST API  

---

## Why Endee?

Endee is a **systems-level vector database** optimized for high-performance  
vector similarity search.

In the open-source version:

- Index creation and ingestion are **engine-managed**
- APIs are primarily used for querying and inspection

This project integrates with Endee **as intended**, without forcing unsupported  
operations.

---

## Project Structure

data/  
└── sample_texts.txt  

src/  
├── embed.py            # Generates embeddings  
└── test_connection.py # Tests Endee connectivity  

requirements.txt  
.gitignore  
README.md  

---

## How to Run the Project

### 1. Start Endee using Docker

docker compose up -d  

Verify it is running:

docker ps  

---

### 2. Set up Python Environment

python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  

---

### 3. Generate Embeddings

python src/embed.py  

This converts text documents into vector embeddings.

---

### 4. Verify Endee Connection

python src/test_connection.py  

A successful response confirms the vector database is running and accessible.

---

## What This Project Demonstrates

- Practical use of vector search  
- Transformer-based semantic embeddings  
- Real integration with a production-grade vector database  
- Dockerized AI infrastructure  

---

## Limitations

- Endee OSS manages index creation internally  
- This project focuses on correct architectural usage, not UI features  

---

## Future Extensions

- Retrieval-Augmented Generation (RAG)  
- Recommendation systems  
- Agentic AI workflows  
- API or frontend layer  

---

## License

This project is provided for educational and evaluation purposes.
