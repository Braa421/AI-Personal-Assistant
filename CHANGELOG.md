# Changelog

All notable changes to this project will be documented in this file.

This project follows Semantic Versioning (SemVer).

---

## [3.2.0] - 2026-07-16

### Added

- Implemented the complete RAG pipeline.
- Connected document retrieval with the request builder.
- Added dynamic context construction from retrieved document chunks.
- Injected retrieved context into LLM requests.
- Improved prompt instructions to encourage grounded responses.
- Separated retrieval, context generation, and request construction into independent modules.

### Tested

- Verified end-to-end RAG pipeline.
- Confirmed responses are generated using retrieved document context.
- Tested semantic retrieval with multiple document topics.
- Verified grounding using custom document content.

---

## [3.1.0] - 2026-07-11

### Added

- Implemented cosine similarity algorithm.
- Added semantic similarity search.
- Built the retrieval engine.
- Added Top-K document retrieval.
- Ranked retrieved chunks by similarity score.

### Tested

- Cosine similarity calculations.
- Semantic document retrieval.
- Top-K ranking.

---

## [3.0.0] - 2026-07-10

### Added

- Initial Retrieval-Augmented Generation (RAG) architecture.
- TXT document loader.
- Text chunking with configurable chunk size and overlap.
- Gemini embedding generation.
- JSON-based vector store.
- Vector persistence utilities.
- Vector store configuration.

### Changed

- Organized RAG components into a dedicated `rag` package.
- Extended project architecture to support document-based retrieval.

### Tested

- TXT document loading.
- Text chunk generation.
- Embedding generation using Gemini.
- Vector serialization to `vectors.json`.

---

## [2.5.0] - 2026-07-07

### Added

- LLM wrapper module.
- Retry mechanism for LLM requests.
- Custom logging system.
- Application log file (`assistant.log`).

### Changed

- Centralized all LLM requests through `llm.py`.
- Improved LLM reliability with automatic retries.
- Improved error handling using `LLMError`.
- Refactored project architecture to separate LLM communication from application logic.

### Tested

- LLM wrapper.
- Retry mechanism.
- LLM exception handling.
- Logging system.

---

## [2.4.0] - 2026-07-07

### Added

- Custom exceptions module.
- ParserError exception.

### Changed

- Refactored LLM JSON parsing to use custom exceptions.
- Improved error handling for memory extraction.

### Tested

- LLM JSON parsing.
- Parser exception handling.
- Memory extraction.
- Relevant memory retrieval.

---

## [2.3.0] - 2026-07-07

### Added

- Safe LLM JSON parser.
- Dedicated LLM parsing module.
- Reusable JSON parsing utility for model responses.

### Changed

- Replaced direct `json.loads()` calls with `parse_llm_json()`.
- Improved JSON parsing reliability for LLM-generated responses.
- Refactored memory-related modules to use the new parser.

### Tested

- Memory extraction.
- Relevant memory retrieval.
- Multiple memory extraction.
- Conversation persistence.
- LLM JSON parsing.

---

## [2.2.0] - 2026-07-07

### Added

- Request builder module.
- Request construction utilities.
- System prompt builder.
- Conversation contents builder.
- Generation configuration builder.

### Changed

- Refactored request construction into a dedicated module.
- Simplified the main application loop.
- Improved project architecture by separating request-building responsibilities.
- Centralized LLM request creation.

### Tested

- Request building.
- System prompt generation.
- Conversation context building.
- Generation configuration.
- End-to-end request pipeline.

---

## [2.1.0] - 2026-07-05

### Added

- Added relevant memory selection.
- The agent now selects only the most relevant long-term memories for each user message.

### Changed

- The system prompt now receives only relevant long-term memory instead of the entire memory store.

### Tested

- Relevant memory selection.
- Memory extraction.
- Memory updates.
- Conversation flow.

---

## [2.0.0] - 2026-07-04

### Added

- Persistent conversation history.
- Conversation loading and saving utilities.
- Custom conversation engine.
- Manual request building.
- Long-term memory persistence.

### Changed

- Replaced SDK chat sessions with manual conversation management.
- Replaced `chat.send_message()` with `client.models.generate_content()`.
- Improved project architecture.
- Simplified request pipeline.

### Tested

- Conversation persistence.
- Conversation context.
- Long-term memory.
- Tool calling.
- Calculator.
- Weather.
- File reader.

---

## [1.5.0] - 2026-07-03

### Added

- Conversation management module.
- Conversation storage.
- Conversation loading.
- Conversation saving.
- Conversation history retrieval.

### Changed

- Refactored project architecture.
- Separated conversation logic from the main application.

---

## [1.0.0] - 2026-07-02

### Added

- Initial AI assistant.
- Google Gemini integration.
- Function calling.
- Memory extraction.
- Memory storage.
- Weather tool.
- Calculator tool.
- File reader.
- Secret code tool.
- System prompt support.

### Initial Release