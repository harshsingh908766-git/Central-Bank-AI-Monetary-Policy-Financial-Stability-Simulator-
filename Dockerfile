
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY pyproject.toml .
COPY src/ ./src/
COPY configs/ ./configs/

RUN pip install --no-cache-dir --no-deps -e .

EXPOSE 8000

CMD [
    "uvicorn",
    "central_bank_ai.main:app",
    "--host",
    "0.0.0.0",
    "--port",
    "8000"
]
