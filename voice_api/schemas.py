from pydantic import BaseModel

class VoiceRequest(BaseModel):
    language: str
    audioFormat: str
    audioBase64: str

class SuccessResponse(BaseModel):
    status: str
    language: str
    classification: str
    confidenceScore: float
    explanation: str

class ErrorResponse(BaseModel):
    status: str
    message: str
