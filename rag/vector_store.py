import json
from config import VECTOR_STORE_FILE
from rag.embeddings import embed_text

def save_vectors(store: list[dict])-> None:
    with open(VECTOR_STORE_FILE, "w") as file:
        json.dump(store, file, indent = 4)

def load_vectors()-> list[dict]:
    try:
        with open(VECTOR_STORE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_document(chunks: list[str])-> None:
    store = load_vectors()

    for chunk in chunks:
        vector = embed_text(chunk)
        store.append(
            {
                "text": chunk,
                "vector": vector
            }
        )
    save_vectors(store)

def clear_vectors()-> None:
    save_vectors([])