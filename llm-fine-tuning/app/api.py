from fastapi import FastAPI
from pydantic import BaseModel
from model.inference import generate_response

app = FastAPI(title="LLM Fine-Tuning Lab API")

class Prompt(BaseModel):
    text: str

@app.post("/infer")
def infer(prompt: Prompt):
    output, score = generate_response(prompt.text)
    return {
        "response": output,
        "confidence": score
    }
