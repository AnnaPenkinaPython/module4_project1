"""poetry, pytest"""
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

    # def __repr__(self):
    #    return f'{self.__name} в наличии, цена: {self.price}, кол-во: {self.quantity}'

    # def __str__(self):
    #    return f'стоимость {self.__name} со скидкой = {self.price * 0.85}'

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


class Phone(Product):
    number_of_sim = []

    def __init__(self, name: str, price: int, quantity: int,
                 number_of_sim: int):  # переопределяем метод базового класса
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
        Phone.number_of_sim.append(self)

    @staticmethod
    def is_zero(self):
        if self.number_of_sim > 0:
            return self.number_of_sim
        if self.number_of_sim <= 0:
            raise Exception(f"ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __add__(self, other):
        return Phone.storage_of_goods + Product.storage_of_goods


class MixinLog:
    def __init__(self, language="EN"):
        self.language = language

    def change_lang(self):
        return self.language == "RU"


class KeyBoard(Product, MixinLog):
    def __init__(self, name: str, price: int, quantity: int, language):
        super().__init__(name, price, quantity)


print(KeyBoard.__mro__)
kb = KeyBoard('Dark Project KD87A', 9600, 5)
print(kb.name, kb.price, kb.quantity)
print(kb.language)
kb.change_lang()
print(kb.language)
