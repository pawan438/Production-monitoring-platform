# Dockerfile
# Backend API container for the Production System Monitoring Platform

FROM python:3.11-slim

WORKDIR /app

# Copy requirements first so Docker can cache this layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend code
COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]