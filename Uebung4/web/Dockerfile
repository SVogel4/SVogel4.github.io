# Uebung4/web/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Abhängigkeiten (falls requirements.txt existiert)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Quellcode kopieren
COPY . /app

EXPOSE 5000

# Default command
CMD ["python", "app.py"]