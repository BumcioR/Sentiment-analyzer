# app/main.py

from fastapi import FastAPI
from app.schemas import InferenceRequest, InferenceResponse

app = FastAPI()

@app.post("/predict", response_model=InferenceResponse)
def predict(request: InferenceRequest) -> InferenceResponse:
    text = request.text

    # tymczasowa logika "predykcji"
    if "great" in text.lower():
        prediction = "positive"
    else:
        prediction = "neutral"

    return InferenceResponse(prediction=prediction)
