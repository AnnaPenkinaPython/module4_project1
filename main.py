"""poetry, pytest"""
# import pandas as pd

# data = pd.read_csv("items.csv")
import csv
import os.path
from errors import InstantiateCSVError


class Item:
    pay_rate = 0.85
    storage_of_goods = []

    def __init__(self, name: str, price: int, quantity: int):
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.storage_of_goods.append(self)

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

    @classmethod
    def instantiate_from_csv(cls, path: str):
        """"Считывает данные из csv-файла и создает экземпляры класса, инициализируя их данными из файла"""
        """Если файл не найден или поврежден выбрасывает соответствующие Exception"""

        path = '../items.csv'
        try:
            with open(path, 'r', encoding='windows-1251', newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    return cls(row['name'], int(row['price']), int(row['quantity']))
        except FileNotFoundError:
            FileNotFoundError("Отсутствует файл item.csv")
        try:
            with open(path, encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if list(row.keys()) == ['name', 'price', 'quantity']:
                        cls(name=row['name'], price=float(row['price']), quantity=int(row['quantity']))
                    else:
                        raise InstantiateCSVError

        except KeyError:
            InstantiateCSVError('Файл items.csv поврежден')


class Phone(Item):
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
        return Phone.storage_of_goods + Item.storage_of_goods


class MixinLog:
    __language = "EN"

    @classmethod
    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

    @property
    def language(self):
        return self.__language


class KeyBoard(Item, MixinLog):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__language = "EN"


print()
