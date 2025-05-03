# app/schemas.py

from pydantic import BaseModel

class InferenceRequest(BaseModel):
    text: str

class InferenceResponse(BaseModel):
    prediction: str
