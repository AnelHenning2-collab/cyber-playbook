from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="SOC Alert Triage API")

class Alert(BaseModel):
    alert_id: str
    description: str
    severity: str

@app.post("/triage")
def triage_alert(alert: Alert):
    # TODO: plug in real RAG + vector DB
    recommendation = f"Prioritize alert {alert.alert_id} with severity {alert.severity}."
    return {
        "summary": f"Synthetic summary for: {alert.description[:120]}...",
        "recommendation": recommendation,
        "confidence": 0.82,
        "citations": []
    }
