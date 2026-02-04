from fastapi import FastAPI, Depends
from voice_api.schemas import VoiceRequest, SuccessResponse, ErrorResponse
from voice_api.utils import verify_api_key, dummy_voice_prediction
from voice_api.config import SUPPORTED_LANGUAGES

app = FastAPI(title="AI Voice Detection API")

@app.post(
    "/api/voice-detection",
    response_model=SuccessResponse,
    responses={401: {"model": ErrorResponse}, 400: {"model": ErrorResponse}}
)
def voice_detection(
    request: VoiceRequest,
    api_key: str = Depends(verify_api_key)
):
    # Validation
    if request.language not in SUPPORTED_LANGUAGES:
        return {
            "status": "error",
            "message": "Unsupported language"
        }

    if request.audioFormat.lower() != "mp3":
        return {
            "status": "error",
            "message": "Only MP3 format is supported"
        }

    # Dummy ML Prediction
    classification, confidence, explanation = dummy_voice_prediction()

    return {
        "status": "success",
        "language": request.language,
        "classification": classification,
        "confidenceScore": confidence,
        "explanation": explanation
    }
