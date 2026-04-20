import streamlit as st
import requests

API_URL = "http://localhost:8003/predict"

st.title("Quantum-Inspired Anomaly Detection Demo")

values = st.text_input("Enter comma-separated numeric values", "0.1, 0.5, 0.9")

if st.button("Run Detection"):
    try:
        vector = [float(v.strip()) for v in values.split(",")]
        resp = requests.post(API_URL, json={"values": vector})
        data = resp.json()

        st.subheader("Prediction")
        st.write(f"Label: {data['label']}")
        st.write(f"Score: {data['score']:.2f}")

    except Exception as e:
        st.error(f"Error: {e}")
