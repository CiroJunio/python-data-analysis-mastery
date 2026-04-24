FROM python:3.11-slim

# Define o diretório de trabalho interno
WORKDIR /app

# Instala dependências de sistema mínimas se necessário
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instala o NumPy e ferramentas de análise
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código para o container
COPY . .

# Por padrão, executa os testes de sanidade ao subir
CMD ["python", "-m", "tests.sanity_check"]