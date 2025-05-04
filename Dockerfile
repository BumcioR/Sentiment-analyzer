FROM python:3.11-slim-bookworm

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY pyproject.toml uv.lock ./

# Copy rest of the application
COPY . .

RUN pip install --upgrade pip && pip install uv
RUN uv pip install --system .

# Expose port
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
