import pytest
from src.product_available import is_product_available

@pytest.mark.parametrize("product_name, quantity, expected_result", [
    ("Chocolate", 3, True),
    ("Granizado", 10, True),
    ("Limon", 0, False),
    ("Dulce de Leche", 5, True),
    ("Fresa", 2, False)
    # Agrega más casos de prueba aquí
])
def test_is_product_available(product_name, quantity, expected_result):
    assert is_product_available(product_name, quantity) == expected_result
