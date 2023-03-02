import pytest
from main import Product
import os

def test_product_repr():
    item = Product('iphone', 100000, 5)
    assert item.__repr__() == 'iphone в наличии, цена: 100000, кол-во: 5'

def test_product_str():
    item = Product('iphone', 100000, 5)
    assert item.__str__() == 'стоимость iphone со скидкой = 85000.0'