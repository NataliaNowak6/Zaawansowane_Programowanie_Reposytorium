def greet(name: str) -> str:
    return f"Hello {name}!"

def calculate_tax(price: float, tax_rate: float = 0.23) -> float:
    return price * tax_rate