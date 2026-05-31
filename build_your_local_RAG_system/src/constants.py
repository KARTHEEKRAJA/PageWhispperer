EMBEDDING_MODEL_PATH = "sentence-transformers/all-mpnet-base-v2"  # OR Path of local eg. "embedding_model/"" or the name of SentenceTransformer model eg. "sentence-transformers/all-mpnet-base-v2" from Hugging Face
ASSYMETRIC_EMBEDDING = False  # Flag for asymmetric embedding
EMBEDDING_DIMENSION = 768  # Embedding model settings
TEXT_CHUNK_SIZE = 300  # Maximum number of characters in each text chunk for

OLLAMA_MODEL_NAME = (
    "llama3.2:1b"  # Name of the model used in Ollama for chat functionality
)

####################################################################################################
# Dont change the following settings
####################################################################################################

# Logging
LOG_FILE_PATH = "logs/app.log"  # File path for the application log file
# OpenSearch settings
OPENSEARCH_HOST = "localhost"  # Hostname for the OpenSearch instance
OPENSEARCH_PORT = 9200  # Port number for OpenSearch
OPENSEARCH_INDEX = "documents"  # Index name for storing documents in OpenSearch

# src/constants.py

# The model used to translate text into vectors
EMBEDDING_MODEL_PATH = "sentence-transformers/all-mpnet-base-v2"

# The size of the vectors (Must be 768 for mpnet-base-v2)
EMBEDDING_DIMENSION = 768

# How many characters per chunk of text
TEXT_CHUNK_SIZE = 500 

# The local LLM running via Ollama
OLLAMA_MODEL_NAME = "llama3.2:1b"
