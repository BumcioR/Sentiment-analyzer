import pytest
from fastapi.testclient import TestClient
from app.main import app
import cloudpickle

client = TestClient(app)


def test_valid_input() -> None:
    response = client.post("/predict", json={"text": "This is amazing!"})
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert isinstance(data["prediction"], str)


def test_invalid_input_empty_string() -> None:
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 422  # Validation error from Pydantic
    data = response.json()
    assert "detail" in data


def test_invalid_input_missing_field() -> None:
    response = client.post("/predict", json={})
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data


def test_model_loading() -> None:
    with open("artifacts/inference_class.pkl", "rb") as f:
        Inference = cloudpickle.load(f)
    inference = Inference("artifacts")
    assert inference is not None


@pytest.mark.parametrize("text", ["I love it!", "Terrible experience.", "It's okay."])
def test_model_inference(text: str) -> None:
    with open("artifacts/inference_class.pkl", "rb") as f:
        Inference = cloudpickle.load(f)
    inference = Inference("artifacts")
    result = inference.predict(text)
    assert isinstance(result, str)
    assert result in ["positive", "negative"]
