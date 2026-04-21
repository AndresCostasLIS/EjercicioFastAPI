FROM python:3.11

WORKDIR /app

# instalar dependencias
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copiar código
COPY . .

# exponer puerto
EXPOSE 8000

# comando de arranque
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]