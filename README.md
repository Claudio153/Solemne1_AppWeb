# Solemne1_AppWeb

Esta aplicación crea una API en python que muestra la hora actual en formato JSON utilizando FASTAPI.

# Instrucciones de uso

## Usando uvicorn

Como requisito es necesario la instalación de poetry:

```bash
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
source ~/.bashrc
```
Luego, para instalar las depencias necesarias, en el directorio del proyecto ejecutar:
```bash
poetry install
```
Finalmente, para ejecutar la aplicación:
```bash
poetry run uvicorn main:app --reload
```

## Usando Docker
```bash
docker pull claudio153/fastapi-app
docker run -d -p 8000:8000 claudio153/fastapi-app
```
Link del docker hub: https://hub.docker.com/r/claudio153/fastapi-app

## Testing con curl
```bash
curl http://127.0.0.1:8000/time
```
