[1mdiff --git a/.gitignore b/.gitignore[m
[1mindex f981fee..b1a015b 100644[m
[1m--- a/.gitignore[m
[1m+++ b/.gitignore[m
[36m@@ -2,4 +2,6 @@[m
 .env[m
 __pycache__/[m
 *.pyc[m
[31m-.vscode/[m
\ No newline at end of file[m
[32m+[m[32m.vscode/[m
[32m+[m[32mmemory.json[m
[32m+[m[32mconversation.json[m
\ No newline at end of file[m
[1mdiff --git a/CHANGELOG.md b/CHANGELOG.md[m
[1mindex b758230..e79155a 100644[m
[1m--- a/CHANGELOG.md[m
[1m+++ b/CHANGELOG.md[m
[36m@@ -1,18 +1,70 @@[m
 # Changelog[m
 [m
[31m-## v1.0 - Initial Release - 2026-07-04[m
[32m+[m[32mAll notable changes to this project will be documented in this file.[m
[32m+[m
[32m+[m[32mThis project follows Semantic Versioning (SemVer).[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32m## [2.0.0] - 2026-07-04[m
 [m
 ### Added[m
[31m-- AI Assistant using Google Gemini[m
[31m-- Tool Calling[m
[31m-- Long-Term Memory[m
[31m-- Calculator Tool[m
[31m-- Weather Tool[m
[31m-- File Reading Tool[m
[31m-[m
[31m-### Project Structure[m
[31m-- main.py[m
[31m-- config.py[m
[31m-- prompts.py[m
[31m-- tools.py[m
[31m-- memory.py[m
[32m+[m
[32m+[m[32m- Persistent conversation history.[m
[32m+[m[32m- Conversation loading and saving utilities.[m
[32m+[m[32m- Custom conversation engine.[m
[32m+[m[32m- Manual request building.[m
[32m+[m[32m- Long-term memory persistence.[m
[32m+[m
[32m+[m[32m### Changed[m
[32m+[m
[32m+[m[32m- Replaced SDK chat sessions with manual conversation management.[m
[32m+[m[32m- Replaced `chat.send_message()` with `client.models.generate_content()`.[m
[32m+[m[32m- Improved project architecture.[m
[32m+[m[32m- Simplified request pipeline.[m
[32m+[m
[32m+[m[32m### Tested[m
[32m+[m
[32m+[m[32m- Conversation persistence.[m
[32m+[m[32m- Conversation context.[m
[32m+[m[32m- Long-term memory.[m
[32m+[m[32m- Tool calling.[m
[32m+[m[32m- Calculator.[m
[32m+[m[32m- Weather.[m
[32m+[m[32m- File reader.[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32m## [1.5.0] - 2026-07-03[m
[32m+[m
[32m+[m[32m### Added[m
[32m+[m
[32m+[m[32m- Conversation management module.[m
[32m+[m[32m- Conversation storage.[m
[32m+[m[32m- Conversation loading.[m
[32m+[m[32m- Conversation saving.[m
[32m+[m[32m- Conversation history retrieval.[m
[32m+[m
[32m+[m[32m### Changed[m
[32m+[m
[32m+[m[32m- Refactored project architecture.[m
[32m+[m[32m- Separated conversation logic from the main application.[m
[32m+[m
[32m+[m[32m---[m
[32m+[m
[32m+[m[32m## [1.0.0] - 2026-07-02[m
[32m+[m
[32m+[m[32m### Added[m
[32m+[m
[32m+[m[32m- Initial AI assistant.[m
[32m+[m[32m- Google Gemini integration.[m
[32m+[m[32m- Function calling.[m
[32m+[m[32m- Memory extraction.[m
[32m+[m[32m- Memory storage.[m
[32m+[m[32m- Weather tool.[m
[32m+[m[32m- Calculator tool.[m
[32m+[m[32m- File reader.[m
[32m+[m[32m- Secret code tool.[m
[32m+[m[32m- System prompt support.[m
[32m+[m
[32m+[m[32m### Initial Release[m
\ No newline at end of file[m
[1mdiff --git a/README.md b/README.md[m
[1mindex a2e5383..95e9e47 100644[m
[1m--- a/README.md[m
[1m+++ b/README.md[m
[36m@@ -1,16 +1,74 @@[m
 # AI Personal Assistant[m
 [m
[31m-An AI assistant built with Python and the Google Gemini API.[m
[32m+[m[32mAn AI-powered personal assistant built with the Google Gemini API.[m
[32m+[m
[32m+[m[32mThe project focuses on building a modular and extensible assistant from scratch instead of relying on built-in SDK chat sessions.[m
 [m
 ## Features[m
 [m
[31m-- Tool Calling[m
[31m-- Long-Term Memory[m
[31m-- File Reading[m
[31m-- Calculator[m
[31m-- Weather Tool[m
[32m+[m[32m- Long-term memory[m
[32m+[m[32m- Persistent conversation history[m
[32m+[m[32m- Function calling (Tools)[m
[32m+[m[32m- Weather tool[m
[32m+[m[32m- Calculator tool[m
[32m+[m[32m- File reader[m
[32m+[m[32m- Custom conversation engine[m
[32m+[m[32m- Modular project architecture[m
[32m+[m[32m- Configurable system prompt[m
[32m+[m
[32m+[m[32m## Project Structure[m
[32m+[m
[32m+[m[32m```[m
[32m+[m[32mAI Personal Assistant/[m
[32m+[m[32m│[m
[32m+[m[32m├── main.py[m
[32m+[m[32m├── config.py[m
[32m+[m[32m├── prompts.py[m
[32m+[m[32m├── memory.py[m
[32m+[m[32m├── conversation.py[m
[32m+[m[32m├── tools.py[m
[32m+[m[32m│[m
[32m+[m[32m├── memory.json[m
[32m+[m[32m├── conversation.json[m
[32m+[m[32m│[m
[32m+[m[32m├── README.md[m
[32m+[m[32m├── CHANGELOG.md[m
[32m+[m[32m└── .gitignore[m
[32m+[m[32m```[m
[32m+[m
[32m+[m[32m## Architecture[m
[32m+[m
[32m+[m[32mThe project is divided into independent modules.[m
[32m+[m
[32m+[m[32m- `config.py` → Application configuration[m
[32m+[m[32m- `memory.py` → Long-term memory management[m
[32m+[m[32m- `conversation.py` → Conversation persistence[m
[32m+[m[32m- `tools.py` → External tools[m
[32m+[m[32m- `prompts.py` → System and memory prompts[m
[32m+[m[32m- `main.py` → Application entry point[m
[32m+[m
[32m+[m[32m## Technologies[m
[32m+[m
[32m+[m[32m- Python 3[m
[32m+[m[32m- Google Gemini API[m
[32m+[m[32m- Function Calling[m
[32m+[m[32m- JSON[m
[32m+[m[32m- Git & GitHub[m
[32m+[m
[32m+[m[32m## Current Version[m
[32m+[m
[32m+[m[32m**v2.0.0**[m
[32m+[m
[32m+[m[32m## Roadmap[m
[32m+[m
[32m+[m[32m- [x] Version 1 — Basic Assistant[m
[32m+[m[32m- [x] Version 1.5 — Conversation Persistence[m
[32m+[m[32m- [x] Version 2.0 — Custom Conversation Engine[m
[32m+[m[32m- [ ] Version 2.1 — Relevant Memory Retrieval[m
[32m+[m[32m- [ ] Version 3.0 — RAG Integration[m
[32m+[m[32m- [ ] Version 4.0 — MCP Support[m
[32m+[m[32m- [ ] Version 5.0 — Desktop Interface[m
 [m
[31m-## Tech Stack[m
[32m+[m[32m## License[m
 [m
[31m-- Python[m
[31m-- Google Gemini API[m
\ No newline at end of file[m
[32m+[m[32mThis project is intended for educational and portfolio purposes.[m
\ No newline at end of file[m
[1mdiff --git a/main.py b/main.py[m
[1mindex 78928c9..702c570 100644[m
[1m--- a/main.py[m
[1m+++ b/main.py[m
[36m@@ -12,39 +12,71 @@[m [mfrom memory import ([m
     update_memory,[m
     extract_memory[m
 )[m
[32m+[m[32mfrom conversation import([m
[32m+[m[32m    load_conversation,[m
[32m+[m[32m    save_conversation,[m
[32m+[m[32m    append_message,[m
[32m+[m[32m    get_recent_conversation[m
[32m+[m[32m)[m
 from google import genai[m
 import json[m
 [m
[32m+[m
 memory = load_memory()[m
[31m-system_prompt = SYSTEM_PROMPT.format(memory = json.dumps(memory, indent = 4))[m
[31m-[m
[31m-chat = client.chats.create([m
[31m-    model = MODEL_NAME,[m
[31m-    config = genai.types.GenerateContentConfig([m
[31m-        system_instruction = system_prompt,[m
[31m-        tools = [[m
[31m-            get_current_time,[m
[31m-            get_secret_code,[m
[31m-            get_weather,[m
[31m-            calculator,[m
[31m-            read_file[m
[31m-        ][m
[31m-    )[m
[31m-    [m
[32m+[m[32mconversation = load_conversation()[m
[32m+[m
[32m+[m[32msystem_prompt = SYSTEM_PROMPT.format([m
[32m+[m[32m    memory=json.dumps(memory, indent=4)[m
 )[m
 [m
[32m+[m[32mprint("Type 'exit' to quit.")[m
 [m
[31m-print ("Type 'exit' to quit.")[m
 while True:[m
     user_message = input("Ask a question: ").strip()[m
[32m+[m
     if user_message == "exit":[m
         break[m
[31m-    elif user_message == "":[m
[31m-        print("Please enter a question or type 'exit' to quit.")[m
[32m+[m
[32m+[m[32m    if user_message == "":[m
[32m+[m[32m        print("Please enter a question.")[m
         continue[m
[31m-    else:[m
[31m-        response = chat.send_message(user_message)[m
[31m-        print(response.text.strip())[m
[31m-        new_data = extract_memory(user_message)[m
[31m-        update_memory(memory, new_data)[m
[31m-        [m
\ No newline at end of file[m
[32m+[m
[32m+[m[32m    # Save user message[m
[32m+[m[32m    append_message(conversation, "user", user_message)[m
[32m+[m
[32m+[m[32m    # Get recent history[m
[32m+[m[32m    recent_conversation = get_recent_conversation(conversation)[m
[32m+[m
[32m+[m[32m    # Build contents[m
[32m+[m[32m    contents = recent_conversation[m
[32m+[m
[32m+[m[32m    # Generate response[m
[32m+[m[32m    try:[m
[32m+[m[32m        response = client.models.generate_content([m
[32m+[m[32m            model=MODEL_NAME,[m
[32m+[m[32m            contents=contents,[m
[32m+[m[32m            config=genai.types.GenerateContentConfig([m
[32m+[m[32m                system_instruction=system_prompt,[m
[32m+[m[32m                tools=[[m
[32m+[m[32m                    get_current_time,[m
[32m+[m[32m                    get_secret_code,[m
[32m+[m[32m                    get_weather,[m
[32m+[m[32m                    calculator,[m
[32m+[m[32m                    read_file,[m
[32m+[m[32m                ][m
[32m+[m[32m            )[m
[32m+[m[32m        )[m
[32m+[m[32m    except Exception as e:[m
[32m+[m[32m        print(e)[m[41m    [m
[32m+[m
[32m+[m[32m    print(response.text.strip())[m
[32m+[m
[32m+[m[32m    # Save assistant message[m
[32m+[m[32m    append_message(conversation, "model", response.text)[m
[32m+[m
[32m+[m[32m    # Update memory[m
[32m+[m[32m    new_data = extract_memory(user_message)[m
[32m+[m[32m    update_memory(memory, new_data)[m
[32m+[m
[32m+[m[32m    # Save conversation[m
[32m+[m[32m    save_conversation(conversation)[m
\ No newline at end of file[m
[1mdiff --git a/memory.json b/memory.json[m
[1mindex 08b813b..5646b47 100644[m
[1m--- a/memory.json[m
[1m+++ b/memory.json[m
[36m@@ -1,4 +1,4 @@[m
 {[m
[31m-    "name": "Braa",[m
[32m+[m[32m    "name": "braa",[m
     "favorite_book": "the avengers"[m
 }[m
\ No newline at end of file[m
