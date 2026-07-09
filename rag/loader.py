from exceptions import UnsupportedFileTypeError

def load_txt(path: str)-> str:
    with open(path, "r", encoding = "utf-8") as file:
        return file.read()

def load_document(path: str)-> str:
    extention = path.split(".")[-1].lower()
    if extention == "txt":
        return load_txt(path)    

    raise UnsupportedFileTypeError(f"Unsupported file type: {path}")