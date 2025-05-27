# Smart-Legal-Assistant-using-RAG



An AI-powered legal assistant that uses Retrieval-Augmented Generation (RAG) to answer questions based on legal documents.

## Features
- Uses Langchain, LlamaIndex, Huggingface
- Answers context-aware legal queries
- Simple CLI interface

## Installation
```bash
pip install -r requirements.txt
```

## Run
```bash
python app.py
```

## Directory Structure
- `legal_docs/` : Add your legal documents here (text format)
- `app.py` : Main application
- `retriever.py` : Vector-based document retriever
- `generator.py` : Huggingface-based RAG model
