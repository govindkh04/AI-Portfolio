from io import BytesIO

from pypdf import PdfReader
from docx import Document


def extract_pdf_text(file_content: bytes) -> str:
    """
    Extract text from a PDF file.
    """

    pdf_file = BytesIO(file_content)
    reader = PdfReader(pdf_file)

    text = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text.append(page_text)

    return "\n".join(text)


def extract_docx_text(file_content: bytes) -> str:
    """
    Extract text from a DOCX file.
    """

    docx_file = BytesIO(file_content)
    document = Document(docx_file)

    text = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text.append(paragraph.text)

    return "\n".join(text)


def extract_text_from_file(
    file_content: bytes,
    filename: str
) -> str:
    """
    Detect the file type and extract its text.
    """

    filename = filename.lower()

    if filename.endswith(".pdf"):
        return extract_pdf_text(file_content)

    if filename.endswith(".docx"):
        return extract_docx_text(file_content)

    raise ValueError(
        "Unsupported file type. Please upload a PDF or DOCX file."
    )