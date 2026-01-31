from Magazine import utils

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        tax = utils.calculate_tax(self.price)
        return f"Product: {self.name}, Price: {self.price}, Tax: {tax:.2f}"

    def greet(self):
        return utils.greet(self.name)