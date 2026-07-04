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

## Project Structure

```
AI Personal Assistant/
│
├── main.py
├── config.py
├── prompts.py
├── memory.py
├── conversation.py
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
- `tools.py` → External tools
- `prompts.py` → System and memory prompts
- `main.py` → Application entry point

## Technologies

- Python 3
- Google Gemini API
- Function Calling
- JSON
- Git & GitHub

## Current Version

**v2.0.0**

## Roadmap

- [x] Version 1 — Basic Assistant
- [x] Version 1.5 — Conversation Persistence
- [x] Version 2.0 — Custom Conversation Engine
- [ ] Version 2.1 — Relevant Memory Retrieval
- [ ] Version 3.0 — RAG Integration
- [ ] Version 4.0 — MCP Support
- [ ] Version 5.0 — Desktop Interface

## License

This project is intended for educational and portfolio purposes.