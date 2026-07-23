import fitz  # PyMuPDF


def load_pdf(pdf_path):
    """
    Load a PDF file and return all its text as a single string.
    """

    try:
        # Open the PDF
        doc = fitz.open(pdf_path)

        text = ""

        # Read every page
        for page_number, page in enumerate(doc, start=1):
            print(f"Reading Page {page_number}...")
            text += page.get_text()

        doc.close()

        return text

    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None