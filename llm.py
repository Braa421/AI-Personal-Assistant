from config import client, MODEL_NAME
from exceptions import LLMError
from config import MAX_RETRIES
from logger import error, info

def generate(contents, config = None):
    for attempt in range(MAX_RETRIES):
        is_last_attempt = attempt == MAX_RETRIES - 1
        try:    
            response = client.models.generate_content(
                model = MODEL_NAME,
                contents = contents,
                config = config
            )
            info("request succeeded.")
            return response
        except Exception as e:
            if is_last_attempt:
                error("Failed to generate LLM response.")
                raise LLMError("Failed to generate LLM response: {e}") from e