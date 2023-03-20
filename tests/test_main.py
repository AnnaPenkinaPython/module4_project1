import pytest
from main import Product, Phone, KeyBoard, MixinLog
import os


def test_cls_keyboard():
    kb = KeyBoard('Dark', 9600, 5)
    assert str(kb) == 'Dark'
    assert str(kb.language) == 'EN'
    kb.change_lang()
    assert str(kb.language) == 'RU'
