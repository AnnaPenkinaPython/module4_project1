"""poetry, pytest"""
from accessify import private, protected
import pandas as pd

data = pd.read_csv("items.csv")


class Product:
    pay_rate = 0.85
    storage_of_goods = []

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        Product.storage_of_goods.append(self)

    @property
    def long_name(self):
        try:
            if len(self.__name) > 10:
                raise Exception
            else:
                return self.__name

        except Exception:
            print("Exception: данное имя превышает количество допустимых символов.")

    @staticmethod
    def is_integer_num(n):
        if isinstance(n, int):
            return True
        if isinstance(n, float):
            return n.is_integer()
        return False

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.pay_rate * self.price
