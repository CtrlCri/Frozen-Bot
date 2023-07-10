import logging

# Configuración básica de logging para mostrar los mensajes en la consola
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1", "heladoFrozen"]

def validate_discount_code(discount_code):
    """
    Valida si un código de descuento se encuentra vigente en la lista.

    :param discount_code: El código de descuento ingresado por el cliente.
    :type discount_code: str

    :return: True si la diferencia entre el código ingresado y los códigos vigentes es menor a tres caracteres
             en al menos uno de los casos. False en caso contrario o si se produce un error durante la validación.
    :rtype: bool
    """
    try:
        return any(len(set(discount_code) ^ set(code)) < 3 for code in _AVAILABLE_DISCOUNT_CODES)
    except Exception as e:
        logger.error(f"Error en la validación del código de descuento: {e}")
        return False

if __name__ == "__main__":
    
    # Ejemplo: Diferencia menor a 3 caracteres
    discount_code = "primavera2021"
    result = validate_discount_code(discount_code)
    print(result)  # Output: True