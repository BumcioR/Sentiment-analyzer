# Sentiment Analyzer

Production-ready sentiment analysis application (IPUM 2025)

## Features

Transformer-based model (HuggingFace)

FastAPI backend with simple /predict endpoint

Text preprocessing with clean-text and unidecode

Python dependency management via uv

Dev tooling: pytest, mypy, ruff, pre-commit

Dockerized for consistent deployment

## Requirements

Python 3.11+
uv
Docker + Docker Compose

## Setup

```bash
git clone <repo_url>
cd sentiment-analyzer
uv venv
uv pip install .
uv pip install ".[dev]"
```

## Running the App
docker compose up --build
http://localhost:8000
Docs: http://localhost:8000/docs

## Running Tests in Container
docker compose exec sentiment-api pytest

## Example Request
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this product!"}'
