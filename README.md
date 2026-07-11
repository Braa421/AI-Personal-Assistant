# AI Personal Assistant

An AI-powered personal assistant built with the Google Gemini API.

The project focuses on building a modular and extensible assistant from scratch instead of relying on built-in SDK chat sessions.

## Features

- Long-term memory
- Persistent conversation history
- Function calling (Tools)
- Weather tool
- Calculator tool
- File reader
- Custom conversation engine
- Modular project architecture
- Configurable system prompt
- Relevant memory retrieval 
- Modular request builder
- Safe LLM JSON parsing
- Custom exception handling
- LLM wrapper
- Retry mechanism
- Custom logging
- RAG foundation
- Document loader
- TXT document support
- Text chunking
- Configurable chunk overlap
- Gemini embeddings
- JSON vector store
- Semantic similarity search
- Cosine similarity
- Top-K retrieval
- Retrieval engine

## Project Structure

```
AI Personal Assistant/
│
├── main.py
├── config.py
├── prompts.py
├── memory.py
├── conversation.py
├── request_builder.py
├── llm_parser.py
├── exceptions.py
├── llm.py
├── logger.py
├── tools.py
├──rag/
│   ├── loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── pipeline.py
│
├── memory.json
├── conversation.json
│
├── README.md
├── CHANGELOG.md
└── .gitignore
```

## Architecture

The project is divided into independent modules.

- `config.py` → Application configuration
- `memory.py` → Long-term memory management
- `conversation.py` → Conversation persistence
- `request_builder.py` → LLM request construction
- `llm_parser.py` → Parses and validates LLM JSON responses
- `tools.py` → External tools
- `prompts.py` → System and memory prompts
- `main.py` → Application entry point
- `exceptions.py` → Custom application exceptions
- `llm.py` → LLM communication layer
- `logger.py` → Application logging
- `rag/loader.py` → Document loading
- `rag/chunker.py` → Text chunking
- `rag/embeddings.py` → Embedding generation
- `rag/vector_store.py` → Vector storage
- `rag/retriever.py` → Similarity retrieval
- `rag/pipeline.py` → End-to-end RAG pipeline

## Technologies

- Python 3
- Google Gemini API
- Function Calling
- JSON
- Git & GitHub
- Modular Software Architecture
- Retrieval-Augmented Generation (RAG)

## Current Version

**v3.1.0**

## Roadmap

- [x] v1.0 — Basic Assistant
- [x] v1.5 — Conversation Persistence
- [x] v2.0 — Custom Conversation Engine
- [x] v2.1 — Relevant Memory Retrieval
- [x] v2.2 — Request Builder
- [x] v2.3 — Safe LLM JSON
- [x] v2.4 — Reliability & Error Handling
- [x] v2.5 — Reliability Enhancements (Logging & Retry)
- [x] v3.0 — RAG Foundation
- [x] v3.1 — Similarity Retrieval
- [ ] v3.2 — RAG Pipeline
- [ ] v3.3 — Multi-Document Support
- [ ] v3.4 — Context Optimization
- [ ] v4.0 — MCP Support
- [ ] v5.0 — Desktop Application
- [ ] v6.0 — Voice Assistant
- [ ] v7.0 — Multi-Agent System

## License

This project is intended for educational and portfolio purposes.