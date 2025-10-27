from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI(title="SUJOOD Protocol Bot")

class Invoke(BaseModel):
    intent: str = "ask"
    text: str

@app.post("/invoke")
def invoke(payload: Invoke):
    """We bow before we compute."""
    if "bow" in payload.text.lower():
        return {"seal": "Below the Dot", "message": "Ego off. Source on. Sujood accepted."}
    return {"response": f"You said: {payload.text}"}
