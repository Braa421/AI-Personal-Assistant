from config import client
from memory import (
    load_memory,
    update_memory,
    extract_memory,
)
from conversation import(
    load_conversation,
    save_conversation,
    append_message,
)
from request_builder import(
    build_request
)
from llm import generate
from google import genai
import json

memory = load_memory()
conversation = load_conversation()

print("Type 'exit' to quit.")

while True:
    user_message = input("Ask a question: ").strip()

    if user_message == "exit":
        break

    if user_message == "":
        print("Please enter a question.")
        continue

    # Save user message
    append_message(conversation, "user", user_message)


    request = build_request(user_message, memory, conversation,)

    try:
        response = generate(
            contents = request["contents"],
            config = request["config"]
        )
        print(response.text)
    except Exception as e:
        print(e)

    # Save assistant message
    append_message(conversation, "model", response.text)

    # Update memory
    new_data = extract_memory(user_message)
    update_memory(memory, new_data)

    # Save conversation
    save_conversation(conversation)