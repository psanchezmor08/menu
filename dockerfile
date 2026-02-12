FROM python:3.9-slim

WORKDIR /app

# Instalamos solo lo estrictamente necesario
# Si el error persiste aquí, es un problema de DNS o Firewall
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8504

CMD ["streamlit", "run", "menu.py", "--server.port=8504", "--server.address=0.0.0.0"]
