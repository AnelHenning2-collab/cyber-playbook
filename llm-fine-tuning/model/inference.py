import numpy as np

def generate_response(text: str):
    text = text.lower()

    # Simple heuristic scoring
    score = float(1 - np.exp(-len(text) / 100))

    # Fake "fine-tuned" behavior
    if "alert" in text:
        output = "This alert indicates suspicious activity. Recommended: investigate user behavior and check SIEM logs."
    elif "phishing" in text:
        output = "This appears to be a phishing attempt. Recommended: block sender and warn affected users."
    else:
        output = "This is a general cybersecurity query. Further context is needed."

    return output, score
