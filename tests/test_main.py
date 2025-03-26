import pytest
from main import ProductPriceTracker
from datetime import datetime

@pytest.fixture
def sample_tracker():
    tracker = ProductPriceTracker("test_products.txt")
    tracker.data = [
        {"name": "Телефон", "date": datetime(2024, 3, 1), "price": 10000},
        {"name": "Телефон", "date": datetime(2024, 3, 15), "price": 10500},
        {"name": "Телефон", "date": datetime(2024, 3, 30), "price": 11000},
    ]
    return tracker

@pytest.mark.parametrize("product_name, expected", [
    ("Телефон", "Зміна ціни за місяць: 1000 грн"),
    ("Ноутбук", "Недостатньо даних для аналізу"),
])
def test_get_price_change(sample_tracker, product_name, expected):
    assert sample_tracker.get_price_change(product_name) == expected
