from fastapi import FastAPI
from pydantic import BaseModel
from model.inference import triage_alert

app = FastAPI(title="SOC Alert Triage API")

class Alert(BaseModel):
    alert_text: str

@app.post("/triage")
def triage(alert: Alert):
    summary, actions, score = triage_alert(alert.alert_text)
    return {
        "summary": summary,
        "recommended_actions": actions,
        "confidence": score
    }
