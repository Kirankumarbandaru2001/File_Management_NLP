import os
from dotenv import load_dotenv
from langchain.adapters import openai

load_dotenv()


from importlib.metadata import metadata
from langchain_openai import OpenAIEmbeddings
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from sentence_transformers import SentenceTransformer
from unstructured.partition.auto import partition

from app.config.settings import REDIS_HOST, REDIS_PORT
import redis

# Initialize Redis client
redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


def parse_document(file_path: str):
    """
    Parses a document to extract text and metadata.
    Args:
    file_path (str): Local path to the document.
    Returns:
    dict: Parsed text and metadata.
    """
    try:
        elements = partition(filename=file_path)
        text = " ".join([element.text for element in elements if hasattr(element, 'text')])

        # Ensure that text is a single string, not a list
        if isinstance(text, list):
            text = " ".join(text)  # Convert list to string if needed

        return {"text": text, "metadata": {}}
    except Exception as e:
        raise RuntimeError(f"Error parsing document: {str(e)}")

def initialize_nlp_chain():
    llm = OpenAI(temperature=0)
    vectorstore = FAISS.load_local("faiss_index")
    qa_chain = RetrievalQA(llm=llm, retriever=vectorstore.as_retriver())
    return qa_chain

def process_query(query:str):
    qa_chain = initialize_nlp_chain()
    response = qa_chain(query)
    return response

# Initialize the Sentence Transformer model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def create_vector_index(parsed_data):
    """
    Create a vector index from the parsed document data.
    Args:
    parsed_data (dict): Parsed document data containing text and metadata.
    Returns:
    object: Vector index object.
    """
    text = parsed_data.get("text")

    # Ensure the text is a string (if it's a list, join it into a single string)
    if isinstance(text, list):
        text = " ".join(text)

    # Example of creating a vector index (adjust according to your actual method)
    try:
        # Assuming you're using OpenAI's embeddings
        embedding = openai.Embedding.create(
            input=text,  # Ensure this is a string, not a list
            model="text-embedding-ada-002"
        )
        return embedding
    except Exception as e:
        raise RuntimeError(f"Error creating vector index: {str(e)}")
