import pytest

from main import Product
import arrs


def test_product_init():
    apple = Product("apple", 100, 5)
    assert apple.name == apple
    assert apple.price == 100
    assert apple.quantity == 5

def test_calculate_total_price():
    assert arrs.calculate_total_price(["orange", 50, 3]) == 150
    assert arrs.calculate_total_price(["orange", 60, 2]) == 120

def test_apply_discount():
    assert arrs.apply_discount(["Iphone", 50000, 4]) == 42500
    assert arrs.apply_discount(["table", 2500, 3]) == 2125


