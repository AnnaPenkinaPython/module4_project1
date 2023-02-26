"""poetry, pytest"""
from accessify import private, protected
# import pandas as pd

# data = pd.read_csv("items.csv")
import csv
import os.path


class Product:
    pay_rate = 0.85
    storage_of_goods = []

    def __init__(self, name: str, price: int, quantity: int):
        self.__name = name
        self.price = price
        self.quantity = quantity
        Product.storage_of_goods.append(self)

    @classmethod
    def instantiate_from_csv(cls, path):
        """Создаёт новые экзэмпляры из csv файла"""
        path = '../items.csv'
        with open(path, 'r', encoding='windows-1251', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                return cls(row['name'], int(row['price']), int(row['quantity']))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) <= 10:
            self.__name = value
        else:
            print('Exception: Длина наименования товара превышает 10 допустимых символов.')

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


