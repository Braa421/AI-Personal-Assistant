import json

def parse_llm_json(text: str)-> dict:
    clean_text = text.strip()
    clean_text = clean_text.replace("```json","")
    clean_text = clean_text.replace("```","")
    return json.loads(clean_text)