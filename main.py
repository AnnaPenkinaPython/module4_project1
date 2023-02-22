"""poetry, pytest"""
from accessify import private, protected
# import pandas as pd

# data = pd.read_csv("items.csv")
import csv


class Product:
    pay_rate = 0.85
    storage_of_goods = []

    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.storage_of_goods.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        """Создаёт новые экзэмпляры из csv файла"""
        copies = []
        with open('items.csv', 'r', encoding="UTF-8", newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                cls(row['name'], int(row['price']), int(row['quantity']))

    @property
    def long_name(self):
        try:
            if len(self.name) > 10:
                raise Exception
            else:
                return self.name

        except Exception:
            print("Данное имя превышает количество допустимых символов.")

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
