import streamlit as st
from pdf_reader import extract_text

st.title("Aytrox")

uploaded_pdf = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_pdf:
    text = extract_text(uploaded_pdf)
    st.subheader("Extracted Text Preview")
    st.text(text[:3000])