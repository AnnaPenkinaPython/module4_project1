import pytest
from main import Product, Phone, KeyBoard, MixinLog
import os




def test_change_lang():
    lang = MixinLog("EN")
    assert lang.change_lang == "RU"
