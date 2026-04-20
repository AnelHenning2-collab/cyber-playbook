from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Phishing Detection API")

class Email(BaseModel):
    subject: str
    body: str

@app.post("/predict")
def predict(email: Email):
    # TODO: replace with real model
    is_phishing = "password" in email.body.lower()
    score = 0.9 if is_phishing else 0.1
    return {
        "label": "phishing" if is_phishing else "legitimate",
        "score": score,
    }
