import logging
import pandas as pd

_PRODUCT_DF = pd.DataFrame({
    "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"], 
    "quantity": [3, 10, 0, 5]
})

# Configuración básica de logging para mostrar los mensajes en la consola
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def is_product_available(product_name, quantity):
    """
    Verifica si un producto está disponible en el inventario.

    :param product_name: Nombre del producto a verificar.
    :type product_name: str
    :param quantity: Cantidad deseada del producto.
    :type quantity: int

    :return: True si el producto está disponible en la cantidad deseada, False en caso contrario.
    :rtype: bool
    """
    try:
        if quantity < 1:
            # Registrar mensaje de error
            logger.error("Producto no disponible")
            return False
        product = _PRODUCT_DF.loc[_PRODUCT_DF["product_name"].str.lower() == product_name.lower(), "quantity"]
        if not product.empty:
            stock = product.iloc[0]
            # Registrar mensaje informativo
            logger.info(f"Producto: {product_name}, Cantidad: {stock}, Disponible: {stock >= quantity}")
            return stock >= quantity
        else:
            # Registrar mensaje de error
            logger.error("Producto no disponible")
            return False
    except Exception as e:
        # Registrar mensaje de excepción
        logger.exception("Ocurrió un error al verificar la disponibilidad del producto: %s", str(e))
        return False
    
if __name__ == "__main__": 
    result = is_product_available("chocolate", 2)
    # Imprimir el resultado
    if result:
        print("¡Hay stock!")
    else:
        print("No hay...")