import json
from config import CONVERSATION_FILE

def load_conversation()-> list:
    try:
        with open(CONVERSATION_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []        

def save_conversation(conversation: list)-> None:
    try:    
        with open(CONVERSATION_FILE, "w") as file:
            json.dump(conversation, file, indent = 4)
    except FileNotFoundError:
        return []

def append_message(conversation: list, role: str, message: str)-> None:
    message_data = {
            "role": role,
            "parts": [
                {
                "text": message
                }
            ]
        }
    conversation.append(message_data)

def get_recent_conversation(conversation: list, limit: int = 10)-> list:
    return conversation[-limit:]