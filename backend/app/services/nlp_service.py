from unstructured.partition.auto import partition

def parse_document(file_path:str):
    """
    Parses a document to extract text and metadata.
    Args:
        file_path (str): Local path to the document.
    Returns:
        dict: Parsed text and metadata.
    """
    try:
        elements = partition(filename = file_path)
        text = " ".join([element.text for element in elements if hasattr(element, 'text')])
        return {"text":text, "metadata":{}}
    except Exception as e:
        raise RuntimeError(f"Error parsing document:{str(e)}")
