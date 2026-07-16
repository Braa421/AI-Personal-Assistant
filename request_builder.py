import json
from google import genai

from config import MODEL_NAME
from prompts import SYSTEM_PROMPT
from memory import retrieve_memory
from conversation import get_recent_conversation
from rag.pipeline import build_context

from tools import (
    get_current_time,
    get_weather,
    calculator,
    read_file
)


def build_system_prompt(user_message: str, memory: dict) -> str:
    relevant = retrieve_memory(user_message, memory)

    return SYSTEM_PROMPT.format(
        memory=json.dumps(relevant, indent=4)
    )


def build_contents(conversation: list, user_message: str, context: str) -> list:
    recent_conversation = get_recent_conversation(conversation)
    recent_conversation.insert(
        -1,
        {
            "role": "user",
            "parts": [
                {"text": f"""You are provided with relevant context retrieved from the user's documents.

                            Answer the question using this context whenever possible.

                            If the answer is not present in the context, clearly state that the information is not available in the provided documents.

                            Context:
                            {context}

                            Question:
                            {user_message}
                            """}
            ]
        }
    )

    return recent_conversation


def build_generation_config(
    system_prompt: str
) -> genai.types.GenerateContentConfig:

    return genai.types.GenerateContentConfig(
        system_instruction=system_prompt,
        tools=[
            get_current_time,
            get_weather,
            calculator,
            read_file
        ]
    )


def build_request(user_message: str, memory: dict, conversation: list) -> dict:

    system_prompt = build_system_prompt(user_message, memory)
    context = build_context(user_message)
    contents = build_contents(conversation, user_message, context)
    config = build_generation_config(system_prompt)

    return {
        "model": MODEL_NAME,
        "contents": contents,
        "config": config
    }