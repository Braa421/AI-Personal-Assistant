from config import client, MODEL_NAME
from prompts import SYSTEM_PROMPT
from tools import (
    get_current_time,
    get_secret_code,
    get_weather,
    calculator,
    read_file
)
from memory import (
    load_memory,
    update_memory,
    extract_memory,
    relevant_memory
)
from conversation import(
    load_conversation,
    save_conversation,
    append_message,
    get_recent_conversation
)
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

    # Get recent history
    recent_conversation = get_recent_conversation(conversation)
    relevant = relevant_memory(user_message, memory)
    system_prompt = SYSTEM_PROMPT.format(
    memory=json.dumps(relevant, indent=4)
    )
    # Build contents
    contents = recent_conversation

    # Generate response
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=contents,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_prompt,
                tools=[
                    get_current_time,
                    get_secret_code,
                    get_weather,
                    calculator,
                    read_file,
                ]
            )
        )
    except Exception as e:
        print(e)    

    print(response.text.strip())

    # Save assistant message
    append_message(conversation, "model", response.text)

    # Update memory
    new_data = extract_memory(user_message)
    update_memory(memory, new_data)

    # Save conversation
    save_conversation(conversation)