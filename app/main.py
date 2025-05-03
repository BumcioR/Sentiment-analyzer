# app/main.py

from fastapi import FastAPI
from app.schemas import InferenceRequest, InferenceResponse
import cloudpickle

# Załaduj model przy starcie serwera (jeden raz, oszczędnie)
with open("app/artifacts/inference_class.pkl", "rb") as f:
    Inference = cloudpickle.load(f)

# Inicjalizacja klasy predykcyjnej – uzupełnimy parametry, gdy je poznamy
inference = Inference()

app = FastAPI()

@app.post("/predict", response_model=InferenceResponse)
def predict(request: InferenceRequest) -> InferenceResponse:
    text = request.text

    # Prawdziwa predykcja z modelu
    prediction = inference.predict(text)

    return InferenceResponse(prediction=prediction)
