import pytest

from src.product_available import is_product_available

def test_is_product_available():
    test_cases = [
        {"product_name": "Chocolate", "quantity": 1, "expected_result": True},
        {"product_name": "Granizado", "quantity": 10, "expected_result": True},
        {"product_name": "Limon", "quantity": 0, "expected_result": False},
        {"product_name": "Dulce de Leche", "quantity": 6, "expected_result": False},
        {"product_name": "Invalid Product", "quantity": 3, "expected_result": False}
    ]

    for test_case in test_cases:
        product_name = test_case["product_name"]
        quantity = test_case["quantity"]
        expected_result = test_case["expected_result"]
        result = is_product_available(product_name, quantity)
        assert result == expected_result
