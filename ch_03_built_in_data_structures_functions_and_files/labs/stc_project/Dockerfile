FROM python:3.11-slim

# Evita a criação de arquivos .pyc e força o log em tempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instala psutil para o sanity_check.py
RUN pip install --no-cache-dir psutil

COPY . /app/

CMD ["python", "run.py"]