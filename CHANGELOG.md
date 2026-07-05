# Changelog

All notable changes to this project will be documented in this file.

This project follows Semantic Versioning (SemVer).

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