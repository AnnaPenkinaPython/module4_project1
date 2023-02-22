import pytest
from main import Product

def test_long_name(product_name):
    with pytest.raises(Exception):
        product_name.name = "Данное имя превышает количество допустимых символов."


def test_is_integer():
    assert Product.is_integer_num(5) is True
    assert Product.is_integer_num(5.0) is True
    assert Product.is_integer_num(5.5) is False

