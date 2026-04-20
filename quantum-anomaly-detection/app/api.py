
from fastapi import FastAPI
from pydantic import BaseModel
from model.inference import predict_anomaly

app = FastAPI(title="Quantum Anomaly Detection API")

class DataPoint(BaseModel):
    values: list

@app.post("/predict")
def predict(data: DataPoint):
    label, score = predict_anomaly(data.values)
    return {
        "label": label,
        "score": score
    }
