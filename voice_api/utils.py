from fastapi import Header, HTTPException
from voice_api.config import API_KEY
import random

def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key or malformed request"
        )

def dummy_voice_prediction():
    classification = random.choice(["AI_GENERATED", "HUMAN"])
    confidence = round(random.uniform(0.75, 0.95), 2)

    explanation = (
        "Unnatural pitch consistency and robotic speech patterns detected"
        if classification == "AI_GENERATED"
        else "Natural pauses and human-like speech variations detected"
    )

    return classification, confidence, explanation
