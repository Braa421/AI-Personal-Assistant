import json
from config import client, MODEL_NAME, MEMORY_FILE
from prompts import MEMORY_PROMPT, MEMORY_SELECTOR_PROMPT

def load_memory()-> dict:
    """
    loads memory from memory.json.
    returns an empty dictionary if the file does not exist
    """    
    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def save_memory(memory: dict)-> None:
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent = 4)

def update_memory(memory: dict, new_data: dict)-> None:
    memory.update(new_data)
    save_memory(memory)
    

def extract_memory(user_message: str)-> dict:
    prompt = MEMORY_PROMPT.format(user_message = user_message)
    memory_response = client.models.generate_content(
        model = MODEL_NAME,
        contents = prompt
    )
    try:
        memory_text = (
            memory_response.text.replace("```json","").replace("```","")
            .strip()
        )
        new_data = json.loads(memory_text)
        return new_data
    except json.JSONDecodeError:
        print("Failed to extract memory.")
        return {}
    
def relevant_memory(user_message: str, memory: dict) -> dict:
    prompt = MEMORY_SELECTOR_PROMPT.format(
        user_message=user_message,
        memory=json.dumps(memory, indent=4)
    )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    result = response.text

    try:
        result = result.replace("```json", "").replace("```", "").strip()
        return json.loads(result)
    except json.JSONDecodeError:
        return {}
