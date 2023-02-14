class Product:
    def __init__(self, name, price, quantity, discount=0.85):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = discount

    storage_of_goods = []
    """для хранения созданных экземпляров класса"""

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.price * self.discount



