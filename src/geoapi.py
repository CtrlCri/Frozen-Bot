import logging
import requests

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GeoAPI:
    """
    Clase para interactuar con la API de información de clima.
    """

    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054" 
    LON = "-61.870523905384076"
    
    MAX_TEMP = 28

    @classmethod
    def is_hot_in_pehuajo(cls):
        """
        Consulta la información de clima y devuelve True si la temperatura actual supera los 28 grados Celsius,
        o False en caso contrario. Devuelve False ante cualquier excepción http.

        :return: True si la temperatura es mayor a 28 grados, False en caso contrario.
        :rtype: bool
        """
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather"
            parameters = {"lat": cls.LAT, "lon": cls.LON, "appid": cls.API_KEY, "units": "metric"}
            response = requests.get(url, parameters)

            if response.status_code == 200:
                data = response.json()
                temperature = data["main"]["temp"]

                # Registrar mensaje informativo
                logger.info(f"La temperatura actual en Pehuajó es {temperature} grados Celsius")

                return temperature > cls.MAX_TEMP
            else:
                # Registrar mensaje de error
                logger.error("No se pudo obtener la información del clima")

                return False
        except requests.exceptions.RequestException:
            # Registrar mensaje de excepción
            logger.exception("Ocurrió un error al realizar la solicitud HTTP")

            return False

if __name__ == "__main__":        
    # Llamar al método is_hot_in_pehuajo para verificar si hace calor en Pehuajó
    result = GeoAPI.is_hot_in_pehuajo()

    # Imprimir el resultado
    if result:
        print("¡Hace calor en Pehuajó!")
    else:
        print("No hace calor en Pehuajó.")

