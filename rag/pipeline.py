from rag.retriever import retrieve

def build_context(query: str)-> str:
    chunks = retrieve(query)
    context = ""
    for chunk in chunks:
        context += chunk["text"] + "\n\n"
    
    return context
    