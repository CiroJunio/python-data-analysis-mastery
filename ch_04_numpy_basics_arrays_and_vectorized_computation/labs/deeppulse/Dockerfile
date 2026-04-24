FROM python:3.11-slim

# Evita arquivos .pyc e buffer de log para clareza no terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependências mínimas para o NumPy (essencial para linalg) 
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir numpy

COPY . .

CMD ["python", "deeppulse/tests/sanity_check.py"]