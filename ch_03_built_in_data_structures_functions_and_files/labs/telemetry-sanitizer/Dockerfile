FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Instala dependências (se houver futuramente)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Comando padrão: apenas mantém o container vivo ou roda o sanity check
CMD ["python", "tests/sanity_check.py"]