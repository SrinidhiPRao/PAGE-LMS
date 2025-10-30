FROM python:3.11-slim

WORKDIR /app

COPY backend ./backend
COPY frontend ./frontend
COPY requirements.txt .
COPY .env .


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
