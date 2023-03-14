import pytest
from main import Product, Phone, KeyBoard, MixinLog
import os


def test_product_repr():
    item = Product('iphone', 100000, 5)
    assert item.__repr__() == 'iphone в наличии, цена: 100000, кол-во: 5'


def test_product_str():
    item = Product('iphone', 100000, 5)
    assert item.__str__() == 'стоимость iphone со скидкой = 85000.0'


def test_is_zero():
    phone = Phone("Iphpne", 10000, 4, 0)
    assert phone.number_of_sim == 0

def test_add():
    phone1 = Phone("Iphpne", 10000, 4, 0)
    product1 = Product("СерыйХолодильник3000", 5000, 4)
    assert phone1.quantity + product1.quantity == 8

def test_change_lang():
    kb = KeyBoard(r)
    assert kb.change_lang ==