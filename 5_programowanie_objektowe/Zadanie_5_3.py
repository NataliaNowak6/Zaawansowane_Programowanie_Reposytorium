# Property (klasa opisująca posiadłość/nieruchomość), posiadająca pola:
# area, rooms (int), price, address
# House (klasa dziedzicząca klasę Property , która opisuje dom), posiadająca pola:
# plot (rozmiar działki, int)
# Flat (klasa dziedzicząca klasę Property , która opisuje mieszkanie), posiadająca pola:
# floor


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


# =========================
# Tworzenie obiektów
# =========================

house = House(
    area=180.5, rooms=6, price=950000, address="Warsaw, Green Street 10", plot=600
)

flat = Flat(area=58.0, rooms=3, price=520000, address="Krakow, Main Square 5", floor=4)

# =========================
# Wyświetlenie obiektów
# =========================

print(house)
print("\n" + "-" * 50 + "\n")
print(flat)
