import pytest
from main import Product
import os

def test_name():
    name1 = Product("СерыйХолодильник3000", 10000, 5)
    assert name1.name == 'Exception: Длина наименования товара превышает 10 допустимых символов.'


def test_is_integer():
    assert Product.is_integer_num(5) is True
    assert Product.is_integer_num(5.0) is True
    assert Product.is_integer_num(5.5) is False

def test_instantiate_from_csv():
    Product.instantiate_from_csv(os.path.join("tests", "test.csv"))
    item = Product.all[-1]
    assert item.name == 'Мышка'
    assert item.price == '50'
    assert item.amount == '5'

