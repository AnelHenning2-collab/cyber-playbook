import streamlit as st
import requests

API_URL = "http://localhost:8000/triage"

st.title("SOC Alert Triage Assistant")

alert_id = st.text_input("Alert ID")
description = st.text_area("Alert description")
severity = st.selectbox("Severity", ["low", "medium", "high", "critical"])

if st.button("Run triage"):
    payload = {
        "alert_id": alert_id or "ALERT-001",
        "description": description,
        "severity": severity,
    }
    resp = requests.post(API_URL, json=payload)
    data = resp.json()
    st.subheader("Summary")
    st.write(data["summary"])
    st.subheader("Recommendation")
    st.write(data["recommendation"])
    st.caption(f"Confidence: {data['confidence']}")
