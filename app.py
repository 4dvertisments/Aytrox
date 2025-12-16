# app.py
import streamlit as st
from pdf_reader import extract_text
from text_utils import chunk_text

st.title("Aytrox")

uploaded_pdf = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_pdf:
    text = extract_text(uploaded_pdf)
    st.subheader("Extracted Text Preview")
    st.text(text[:3000])

    chunks = chunk_text(text)
    st.subheader("Number of Chunks")
    st.text(len(chunks))
