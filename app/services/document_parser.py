from pypdf import PdfReader
from docx import Document


class DocumentParser:

    @staticmethod
    def read_pdf(file):

        text = ""

        try:
            pdf = PdfReader(file)

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        except Exception as e:
            raise Exception(
                f"Error reading PDF: {str(e)}"
            )

        return text

    @staticmethod
    def read_docx(file):

        try:
            document = Document(file)

            text = "\n".join(
                paragraph.text
                for paragraph in document.paragraphs
                if paragraph.text.strip()
            )

            return text

        except Exception as e:
            raise Exception(
                f"Error reading DOCX: {str(e)}"
            )

    @staticmethod
    def read_txt(file):

        try:
            return file.read().decode("utf-8")

        except Exception as e:
            raise Exception(
                f"Error reading TXT: {str(e)}"
            )

    @staticmethod
    def extract_text(uploaded_file):

        file_name = uploaded_file.name.lower()

        if file_name.endswith(".pdf"):
            return DocumentParser.read_pdf(uploaded_file)

        elif file_name.endswith(".docx"):
            return DocumentParser.read_docx(uploaded_file)

        elif file_name.endswith(".txt"):
            return DocumentParser.read_txt(uploaded_file)

        else:
            raise ValueError(
                "Unsupported file format"
            )