from modules.pdf_loader import load_pdf
from modules.text_splitter import split_text
from modules.embeddings import create_embedding_model
from modules.vector_store import create_vector_store


def main():

    pdf_path = "data/SARATH_nul.pdf"

    pdf_text = load_pdf(pdf_path)

    if not pdf_text:
        return

    chunks = split_text(pdf_text)

    print(f"Chunks Created: {len(chunks)}")

    embedding_model = create_embedding_model()

    print("\nCreating Vector Database...\n")

    vector_store = create_vector_store(
        chunks,
        embedding_model
    )

    print("Vector Database Created Successfully!")
    print(f"Stored {len(chunks)} chunks.")


if __name__ == "__main__":
    main()