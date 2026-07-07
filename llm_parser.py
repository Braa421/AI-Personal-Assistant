import json
from exceptions import ParserError

def parse_llm_json(text: str)-> dict:
    clean_text = text.strip()
    clean_text = clean_text.replace("```json","")
    clean_text = clean_text.replace("```","")
    try:
        return json.loads(clean_text)
    except Exception as e:
        raise ParserError("Failed to parse LLM JSON response.") from e