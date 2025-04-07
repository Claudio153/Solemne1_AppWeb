import sys
from datetime import datetime

from fastapi.testclient import TestClient
from main import app  # Ahora importamos directamente desde solemne1

client = TestClient(app)


def test_get_time():
    response = client.get("/time")

    data = response.json()
    assert "current_time" in data  # Verifica que el JSON tiene la clave esperada

    # Verifica que el formato del tiempo sea correcto
    try:
        datetime.strptime(data["current_time"], "%Y-%m-%d %H:%M:%S")
    except ValueError:
        assert False, "El formato de la fecha es incorrecto"
