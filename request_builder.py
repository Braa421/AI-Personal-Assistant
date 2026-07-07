import json
from google import genai
from config import client, MODEL_NAME
from prompts import SYSTEM_PROMPT
from memory import retrieve_memory
from conversation import get_recent_conversation
from tools import (
    get_current_time,
    get_weather,
    calculator,
    read_file
)

def build_system_prompt(user_message: str, memory: dict)-> str:
    relevant = retrieve_memory(user_message, memory)
    system_prompt = SYSTEM_PROMPT.format(
    memory=json.dumps(relevant, indent=4))
    return system_prompt

def build_contents(conversation: list)-> list:
    recent_conversation = get_recent_conversation(conversation)
    contents = recent_conversation
    return contents

def build_generation_config(system_prompt: str)-> genai.types.GenerateContentConfig:
    config=genai.types.GenerateContentConfig(
                system_instruction=system_prompt,
                tools=[
                    get_current_time,
                    get_weather,
                    calculator,
                    read_file
                ]
            )
    return config

def build_request(user_message: str, memory: dict, conversation: list)-> dict:
    system_prompt = build_system_prompt(user_message, memory)
    contents = build_contents(conversation)
    config = build_generation_config(system_prompt)
    
    request = {
        "model": MODEL_NAME,
        "contents": contents,
        "config": config
    }
    return request
