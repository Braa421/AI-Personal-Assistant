from datetime import datetime
from config import LOG_FILE

def log(level: str, message: str)-> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as file:
        file.write(
            f"==============================\n----------\nTime     : {timestamp}\nLevel    : {level}\nMessage  : {message}\n----------\n==============================\n"
        )

def info(message: str)-> None:
    log("INFO", message)

def error(message: str)-> None:
    log("ERROR", message)
