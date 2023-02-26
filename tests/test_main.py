import pytest
from main import Product
import os

def test_name():
    name1 = Product("Серыйхолодильник3000", 10000, 5)
    assert name1.name == 'Серыйхолодильник3000'


def test_is_integer():
    assert Product.is_integer_num(5) is True
    assert Product.is_integer_num(5.0) is True
    assert Product.is_integer_num(5.5) is False

def test_instantiate_from_csv():
    item = Product.instantiate_from_csv(os.path.join("tests", "test.csv"))

    assert item.name == 'Смартфон'
    assert item.price == 100
    assert item.quantity == 1

