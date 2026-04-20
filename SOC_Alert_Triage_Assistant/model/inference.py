import numpy as np
from model.retriever import retrieve_context

def triage_alert(alert_text: str):
    context = retrieve_context(alert_text)

    # Simple heuristic scoring
    score = float(1 - np.exp(-len(alert_text) / 120))

    summary = f"Detected alert pattern: {context}"
    actions = (
        "1. Validate the source IP.\n"
        "2. Check for repeated failed logins.\n"
        "3. Review user activity in SIEM.\n"
        "4. Escalate if lateral movement is detected."
    )

    return summary, actions, score
