# app/schemas.py

from pydantic import BaseModel, Field

class InferenceRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Input text must be a non-empty string")

class InferenceResponse(BaseModel):
    prediction: str
