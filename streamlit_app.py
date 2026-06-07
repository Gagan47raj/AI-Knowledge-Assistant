import streamlit as st
import ollama

from app.services.document_parser import DocumentParser
from app.services.chunking_service import ChunkingService

st.set_page_config(
    page_title="AI Knowledge Assistant",
    layout="wide"
)

st.title("📄 AI Knowledge Assistant")

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX or TXT",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:

    try:

        parser = DocumentParser()

        text = parser.extract_text(
            uploaded_file
        )

        st.success(
            "Document parsed successfully"
        )

        # Document Statistics
        st.subheader(
            "Document Information"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Characters",
                len(text)
            )

        with col2:
            st.metric(
                "Words",
                len(text.split())
            )

        # Preview
        st.subheader("Preview")

        st.text_area(
            "Extracted Text",
            text[:5000],
            height=300
        )

        # Chunking
        chunk_service = ChunkingService()

        chunks = chunk_service.chunk_text(
            text
        )

        st.subheader(
            "Chunk Information"
        )

        st.metric(
            "Total Chunks",
            len(chunks)
        )

        # Ask Questions
        st.divider()

        st.subheader(
            "Ask Questions About This Document"
        )

        question = st.text_input(
            "Enter your question"
        )

        if st.button("Ask"):

            if not question.strip():

                st.warning(
                    "Please enter a question."
                )

            else:

                with st.spinner(
                    "Thinking..."
                ):

                    prompt = f"""
You are a document assistant.

Answer ONLY using the document content below.

If the answer is not present in the document,
reply with:
"I could not find that information in the document."

Document:
{text}

Question:
{question}

Answer:
"""

                    response = ollama.chat(
                        model="mistral",
                        messages=[
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ]
                    )

                    answer = response["message"]["content"]

                    st.subheader(
                        "Answer"
                    )

                    st.write(answer)

        # View Chunks
        with st.expander(
            "View Chunks"
        ):

            for idx, chunk in enumerate(chunks):

                st.markdown(
                    f"### Chunk {idx + 1}"
                )

                st.write(chunk)

                st.divider()

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )