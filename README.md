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
├── tools.py
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

## Technologies

- Python 3
- Google Gemini API
- Function Calling
- JSON
- Git & GitHub
- Modular Software Architecture

## Current Version

**v2.4.0**

## Roadmap

- [x] v1.0 — Basic Assistant
- [x] v1.5 — Conversation Persistence
- [x] v2.0 — Custom Conversation Engine
- [x] v2.1 — Relevant Memory Retrieval
- [x] v2.2 — Request Builder
- [x] v2.3 — Safe LLM JSON
- [x] v2.4 — Reliability & Error Handling
- [ ] v2.5 — Reliability Enhancements (Logging & Retry)
- [ ] v3.0 — RAG Integration
- [ ] v4.0 — MCP Support
- [ ] v5.0 — Desktop Interface

## License

This project is intended for educational and portfolio purposes.