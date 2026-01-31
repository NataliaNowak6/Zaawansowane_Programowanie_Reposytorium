from Classes.Brewery import fetch_breweries
from Classes.Library import Library
from Classes.Order_system import Employee, Student, Book, Order
from Classes.Property_system import House, Flat
from datetime import date

def main():
    # ---- Przykład Brewery ----
    breweries = fetch_breweries(5)
    for b in breweries:
        print(b)
        print("-" * 40)

    # ---- Przykład Library ----
    lib = Library("Warsaw", "Main Street", "00-001", "8:00-18:00", "123456789")
    emp = Employee("Anna", "Kowalska", date(2020, 5, 1), date(1990, 3, 12), "Warsaw", "Green 3", "00-002", "111111111")
    stu = Student("Jan", "Kowalski", "S001", "444444444")
    book = Book(lib, date(2010, 6, 1), "Adam", "Mickiewicz", 320)
    order = Order(emp, stu, [book], date.today())
    print(order)

    # ---- Przykład Property ----
    house = House(180, 6, 950000, "Warsaw, Green Street 10", 600)
    flat = Flat(58, 3, 520000, "Krakow, Main Square 5", 4)
    print(house)
    print(flat)


if __name__ == "__main__":
    main()