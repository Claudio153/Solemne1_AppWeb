
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install poetry

# Instala las dependencias 
RUN poetry install --no-root

# Expone el puerto 8000
EXPOSE 8000

# Comando para correr la app
CMD ["poetry", "run", "uvicorn", "src.solemne1.main:app", "--host", "localhost/time", "--port", "8000"]
