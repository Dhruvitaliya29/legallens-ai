import streamlit as st


st.set_page_config(
    page_title="LegalLens AI",
    page_icon="⚖️",
    layout="wide",
)

st.title("LegalLens AI")
st.write(
    "AI-powered legal document analysis and grounded question answering."
)

uploaded_file = st.file_uploader(
    "Upload a legal document",
    type=["pdf"],
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

    st.info(
        "Document ingestion pipeline will be connected here."
    )