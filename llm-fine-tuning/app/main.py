import streamlit as st
import requests

API_URL = "http://localhost:8005/infer"

st.title("LLM Fine-Tuning Lab")

prompt = st.text_area("Enter a prompt for the fine-tuned model")

if st.button("Generate Response"):
    resp = requests.post(API_URL, json={"text": prompt})
    data = resp.json()

    st.subheader("Model Output")
    st.write(data["response"])

    st.subheader("Confidence Score")
    st.write(f"{data['confidence']:.2f}")
