# AI for Fraud Detection – AI Generated Voice Detection

This project implements a REST-based AI Voice Detection system that classifies whether a given voice sample is **AI-generated** or **human**.

The system is designed according to the provided problem statement and exposes a secure FastAPI endpoint for voice analysis.

---

## 🚀 Features

- Accepts **Base64-encoded MP3 audio**
- Supports multiple languages:
  - Hindi
  - English
  - Tamil
  - Telugu
  - Malayalam
- Detects whether the voice is **HUMAN** or **AI_GENERATED**
- Returns a **confidence score** (0–1)
- Provides a short **explanation** for the prediction
- API key–protected endpoint
- Swagger UI for easy testing

---

## 🧠 System Architecture
voice_api/
├── main.py # FastAPI application and endpoint
├── schemas.py # Request and response schemas
├── utils.py # API key validation
├── config.py # Configuration and constants
└── ml/
├── decoder.py # Base64 → MP3 decoding
├── preprocess.py # Audio loading and preprocessing
├── features.py # Feature extraction (MFCC)
├── model.py # ML model loading/training
└── predict.py # Voice prediction logic


---

## 🔍 How Prediction Works

1. The Base64-encoded MP3 audio is decoded.
2. Audio is preprocessed and resampled.
3. Acoustic features (MFCC) are extracted.
4. A machine learning model performs inference.
5. The system returns:
   - Classification (`HUMAN` or `AI_GENERATED`)
   - Confidence score
   - Explanation of the decision

⚠️ No hard-coded rules are used for prediction.

---

## 🔐 API Authentication

All requests must include an API key in the header:



x-api-key: sk_test_123456789


Invalid or missing keys return a `401 Unauthorized` response.

---

## 📡 API Endpoint

### POST `/api/voice-detection`

**Request Body**
```json
{
  "language": "Hindi",
  "audioFormat": "mp3",
  "audioBase64": "<BASE64_MP3_STRING>"
}


Successful Response

{
  "status": "success",
  "language": "Hindi",
  "classification": "HUMAN",
  "confidenceScore": 0.87,
  "explanation": "Natural pauses and human-like speech variations detected"
}

🧪 Testing

The API was tested using real MP3 audio samples

Audio files were converted to Base64 and tested via Swagger UI

Swagger available at:

/docs

🏁 Conclusion

This system fully complies with the problem statement requirements, provides a secure and scalable API, and demonstrates real-time AI-based voice fraud detection using audio signal processing and machine learning.


# ❓ **Explanation KAHAN likhni hoti hai? (MOST IMPORTANT)**

### 👉 **Explanation README me nahi likhte**
### 👉 **Explanation API RESPONSE ka part hoti hai**

#### 📍 Actual explanation generate hoti hai yahan:
voice_api/ml/predict.py


Example:
```python
return (
    "HUMAN",
    confidence,
    "Natural pauses and human-like speech variations detected"
)


The project follows a **modular architecture** separating API and ML logic:

