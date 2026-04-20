import streamlit as st
import requests

API_URL = "http://localhost:8004/triage"

st.title("SOC Alert Triage Assistant")

alert_text = st.text_area("Paste alert text")

if st.button("Analyze Alert"):
    resp = requests.post(API_URL, json={"alert_text": alert_text})
    data = resp.json()

    st.subheader("Summary")
    st.write(data["summary"])

    st.subheader("Recommended Actions")
    st.write(data["recommended_actions"])

    st.subheader("Confidence Score")
    st.write(f"{data['confidence']:.2f}")
