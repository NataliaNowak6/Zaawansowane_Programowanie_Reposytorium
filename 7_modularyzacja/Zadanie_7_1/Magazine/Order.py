from Magazine import utils
from Magazine.Product import Product
from datetime import date

class Order:
    def __init__(self, products: list[Product], customer: str):
        self.products = products
        self.customers = customer
        self.order_date = date.today()

    def total_price(self) -> float:
        return sum(product.price for product in self.products)

    def __str__(self) -> str:
        product_list = "\n".join(str(p) for p in self.products)
        return (
            f"Order for {self.customers} on {self.order_date}:\n"
            f"{product_list}\n"
            f"Total price: {self.total_price():.2f}"
        )

    def greet_customer(self):
        return utils.greet(self.customers)