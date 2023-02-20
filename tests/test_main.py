
from main import Product


def test_product_init():
    apple = Product("apple", 100, 5)
    assert apple.name == "apple"
    assert apple.price == 100
    assert apple.quantity == 5


def test_with_orange():
    orange = Product("orange", 50, 3)
    assert orange.calculate_total_price() == 150
    assert orange.apply_discount() == 42.5


def test_with_iphone():
    Iphone = Product("Iphone", 50000, 4)
    assert Iphone.calculate_total_price() == 200000
    assert Iphone.apply_discount() == 42500
