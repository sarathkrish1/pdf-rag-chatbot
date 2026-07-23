from langchain_ollama import OllamaEmbeddings


def create_embedding_model():
    """
    Create and return the Ollama embedding model.
    """
    embedding_model = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    return embedding_model