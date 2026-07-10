from config import client, EMBEDDING_MODEL

def embed_text(text: str)-> list[float]:
    response = client.models.embed_content(
        model = EMBEDDING_MODEL,
        contents = text
    )
    return response.embeddings[0].values