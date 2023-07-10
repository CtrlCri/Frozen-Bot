import pytest
from src.validate_code import validate_discount_code

test_cases = {
    "Test Case 1": {
        "discount_code": "primavera2021",
        "expected_result": True
    },
    "Test Case 2": {
        "discount_code": "Helado2021",
        "expected_result": False
    },
    "Test Case 3": {
        "discount_code": "Navidad2x2",
        "expected_result": True
    },
    "Test Case 4": {
        "discount_code": "Verano2021",
        "expected_result": True
    },
    "Test Case 5": {
        "discount_code": "NAVIDAD2X1",
        "expected_result": False
    },
    # Agrega más casos de prueba aquí
}

@pytest.mark.parametrize("test_name, test_data", test_cases.items())
def test_validate_discount_code(test_name, test_data):
    discount_code = test_data["discount_code"]
    expected_result = test_data["expected_result"]

    assert validate_discount_code(discount_code) == expected_result
