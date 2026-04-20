cyber-playbook/
  index.html
  assets/
import streamlit as st
import requests

API_URL = "http://localhost:8001/predict"

st.title("Phishing Detection Demo")

subject = st.text_input("Email subject")
body = st.text_area("Email body")

if st.button("Classify"):
    payload = {"subject": subject, "body": body}
    resp = requests.post(API_URL, json=payload)
    data = resp.json()
    st.subheader("Prediction")
    st.write(f"Label: {data['label']}")
    st.write(f"Score: {data['score']:.2f}")
  phishing-detection/
    index.html
    app/
      main.py
      api.py
      requirements.txt
      Dockerfile
    model/
      train.py
      inference.py
      config.yaml
    notebooks/
    docs/

  soc-alert-triage/
    index.html
    app/
    model/
    notebooks/
    docs/

  llm-fine-tuning/
    index.html
    app/
    model/
    notebooks/
    docs/

  multimodal-security/
    index.html
    app/
    model/
    notebooks/
    docs/

  quantum-anomaly/
    index.html
    app/
    model/
    notebooks/
    docs/
