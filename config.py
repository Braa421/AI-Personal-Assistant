from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL_NAME = "gemini-2.5-flash"
MEMORY_FILE = "memory.json"
CONVERSATION_FILE = "conversation.json"
LOG_FILE = "assistant.log"
MAX_RETRIES = 3

client = genai.Client(
    api_key = API_KEY
)