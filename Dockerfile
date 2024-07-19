# Usar imagem base do Python
FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY requirements.txt requirements.txt

# Instalar dependências
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copiar todo o projeto para o diretório de trabalho
COPY . .

# Definir variáveis de ambiente
ENV FLASK_APP=services.py
ENV CELERY_BROKER_URL=redis://redis:6379/0
ENV CELERY_RESULT_BACKEND=redis://redis:6379/0

# Comando para rodar o aplicativo
CMD ["flask", "run", "--host=0.0.0.0"]