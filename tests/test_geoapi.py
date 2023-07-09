import pytest  # Una biblioteca para hacer pruebas en Python
from src.geoapi import GeoAPI  # Importar la clase GeoAPI desde el archivo geoapi.py
import requests  # Una biblioteca para hacer solicitudes de HTTP

# Clase simulada para representar una respuesta HTTP
class MockResponse:
    def __init__(self, status_code, json_data=None):
        self.status_code = status_code
        self.json_data = json_data

    def json(self):
        return self.json_data

# Fixture que se ejecuta automáticamente antes de cada prueba
@pytest.fixture(autouse=True)
def mock_requests_get(monkeypatch):
    # Función simulada para reemplazar requests.get y devolver respuestas simuladas
    def mock_get(url, params):
        # Simular una respuesta exitosa con una temperatura alta para Pehuajó
        if params.get("lat") == GeoAPI.LAT and params.get("lon") == GeoAPI.LON:
            json_data = {
                "main": {
                    "temp": GeoAPI.MAX_TEMP + 1
                }
            }
            return MockResponse(200, json_data)
        # Simular una respuesta exitosa con una temperatura baja para otras coordenadas
        elif params.get("lat") == "0" and params.get("lon") == "0":
            json_data = {
                "main": {
                    "temp": 0
                }
            }
            return MockResponse(200, json_data)
        # Simular una respuesta fallida para coordenadas inexistentes
        else:
            return MockResponse(500)

    # Reemplazar la función requests.get con nuestra función simulada
    monkeypatch.setattr(requests, "get", mock_get)


# Prueba para verificar si hace calor en Pehuajó
def test_is_hot_in_pehuajo():
    # Llamar al método estático is_hot_in_pehuajo
    result = GeoAPI.is_hot_in_pehuajo()

    # Verificar que el resultado sea verdadero (hace calor en Pehuajó)
    assert result is True


# Prueba para verificar si no hace calor en Pehuajó
def test_is_not_hot_in_pehuajo():
    # Llamar al método estático is_hot_in_pehuajo con otras coordenadas
    result = GeoAPI.is_hot_in_pehuajo()

    # Verificar que el resultado sea verdadero (no hace calor en Pehuajó)
    assert result is True


# Prueba para verificar si se produce un error HTTP
def test_http_error():
    # Llamar al método estático is_hot_in_pehuajo con coordenadas inexistentes
    result = GeoAPI.is_hot_in_pehuajo()

    # Verificar que el resultado sea verdadero debido a un error HTTP
    assert result is True


