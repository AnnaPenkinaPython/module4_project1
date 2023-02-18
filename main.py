"""poetry, pytest"""


class Product:
    price = input()
    pay_rate = 0.85
    storage_of_goods = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.storage_of_goods.append(self)

    """для хранения созданных экземпляров класса"""

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.pay_rate * self.price
