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
    extract_memory
)
from google import genai
import json

memory = load_memory()
system_prompt = SYSTEM_PROMPT.format(memory = json.dumps(memory, indent = 4))

chat = client.chats.create(
    model = MODEL_NAME,
    config = genai.types.GenerateContentConfig(
        system_instruction = system_prompt,
        tools = [
            get_current_time,
            get_secret_code,
            get_weather,
            calculator,
            read_file
        ]
    )
    
)


print ("Type 'exit' to quit.")
while True:
    user_message = input("Ask a question: ").strip()
    if user_message == "exit":
        break
    elif user_message == "":
        print("Please enter a question or type 'exit' to quit.")
        continue
    else:
        response = chat.send_message(user_message)
        print(response.text.strip())
        new_data = extract_memory(user_message)
        update_memory(memory, new_data)
        