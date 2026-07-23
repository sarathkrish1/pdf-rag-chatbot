from langchain_chroma import Chroma
from langchain_core.documents import Document


def create_vector_store(chunks, embedding_model):
    """
    Store document chunks in ChromaDB.
    """

    documents = []

    for chunk in chunks:
        documents.append(Document(page_content=chunk))

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory="chroma_db"
    )

    return vector_store