# Sentiment Analyzer

Production-ready sentiment analysis application (IPUM 2025)

## Features

- FastAPI backend with single-text sentiment inference
- Transformer-based model (HuggingFace)
- Clean and preprocessed input using `clean-text`
- Uses `uv` for dependency management
- Dev tooling: `pytest`, `ruff`, `mypy`, pre-commit hooks

## Setup

```bash
uv venv
uv pip install .
uv pip install ".[dev]"
```
