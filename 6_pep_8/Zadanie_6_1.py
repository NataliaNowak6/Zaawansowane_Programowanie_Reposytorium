#Dotychczasowy stworzony kod (na wszystkich branchach) dostosować do standardu PEP8, tak żeby moduł pycodestyle nie zwracał żadnych warningów, ani errorów.

class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return (
            f"House:\n"
            f"  Address: {self.address}\n"
            f"  Area: {self.area} m²\n"
            f"  Rooms: {self.rooms}\n"
            f"  Plot size: {self.plot} m²\n"
            f"  Price: {self.price} PLN"
        )


class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return (
            f"Flat:\n"
            f"  Address: {self.address}\n"
            f"  Area: {self.area} m²\n"
            f"  Rooms: {self.rooms}\n"
            f"  Floor: {self.floor}\n"
            f"  Price: {self.price} PLN"
        )


house = House(180.5, 6, 950_000, "Warsaw, Green Street 10", 600)
flat = Flat(58.0, 3, 520_000, "Krakow, Main Square 5", 4)

print(house)
print("\n" + "-" * 50 + "\n")
print(flat)
