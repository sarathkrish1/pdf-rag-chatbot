from modules.pdf_loader import load_pdf
from modules.text_splitter import split_text


def main():
    pdf_path = "data/SARATH_nul.pdf"

    pdf_text = load_pdf(pdf_path)

    if pdf_text:
        chunks = split_text(pdf_text)

        print(f"\nTotal Chunks: {len(chunks)}\n")

        for i, chunk in enumerate(chunks, start=1):
            print("=" * 60)
            print(f"Chunk {i}")
            print("=" * 60)
            print(chunk)
            print()

    else:
        print("Failed to load PDF.")


if __name__ == "__main__":
    main()