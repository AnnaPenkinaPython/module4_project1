import pytest
from main import Product



def test_product_init():
    apple = Product("apple", 100, 5)
    assert apple.name == apple
    assert apple.price == 100
    assert apple.quantity == 5

def test_calculate_total_price():
    orange = Product("orange", 50, 3)
    assert orange.calculate_total_price() == 150
    assert orange. calculate_total_price() == 120

def test_apply_discount():
    Iphone = Product("Iphone", 50000, 4)
    table = Product("table", 2500, 3)
    assert Iphone.apply_discount() == 42500
    assert table.apply_discount() == 2125



