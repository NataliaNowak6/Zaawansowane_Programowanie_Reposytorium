# Stworzyć następujące klasy:
# Library (klasa opisująca bibliotekę), posiadająca pola:
# city, street, zip_code, open_hours (str), phone
# Employee (klasa opisująca pracownika biblioteki), posiadająca pola:
# first_name, last_name, hire_date, birth_date, city, street, zip_code, phone
# Book (klasa opisująca książkę), posiadająca pola:
# library, publication_date, author_name, author_surname, number_of_pages
# Order (klasa opisująca zamówienie), posiadająca pola:
# employee, student, books (lista obiektów klasy Book), order_date

from datetime import date
from typing import List


class Library:
    def __init__(
        self, city: str, street: str, zip_code: str, open_hours: str, phone: str
    ):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return (
            f"Library:\n"
            f"  Address: {self.street}, {self.zip_code} {self.city}\n"
            f"  Open hours: {self.open_hours}\n"
            f"  Phone: {self.phone}"
        )


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: date,
        birth_date: date,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return (
            f"Employee:\n"
            f"  Name: {self.first_name} {self.last_name}\n"
            f"  Birth date: {self.birth_date}\n"
            f"  Hire date: {self.hire_date}\n"
            f"  Address: {self.street}, {self.zip_code} {self.city}\n"
            f"  Phone: {self.phone}"
        )


class Student:
    def __init__(self, first_name: str, last_name: str, student_id: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.phone = phone

    def __str__(self) -> str:
        return (
            f"Student:\n"
            f"  Name: {self.first_name} {self.last_name}\n"
            f"  Student ID: {self.student_id}\n"
            f"  Phone: {self.phone}"
        )


class Book:
    def __init__(
        self,
        library: Library,
        publication_date: date,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return (
            f"Book:\n"
            f"  Author: {self.author_name} {self.author_surname}\n"
            f"  Publication date: {self.publication_date}\n"
            f"  Pages: {self.number_of_pages}\n"
            f"  Available in:\n{self.library}"
        )


class Order:
    def __init__(
        self, employee: Employee, student: Student, books: List[Book], order_date: date
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        books_str = "\n\n".join(str(book) for book in self.books)
        return (
            f"Order:\n"
            f"Order date: {self.order_date}\n\n"
            f"{self.employee}\n\n"
            f"{self.student}\n\n"
            f"Books:\n{books_str}"
        )


# =========================
# Tworzenie obiektów
# =========================

library1 = Library("Warsaw", "Main Street 1", "00-001", "8:00–18:00", "123456789")
library2 = Library("Krakow", "Old Town 5", "30-001", "9:00–17:00", "987654321")

employees = [
    Employee(
        "Anna",
        "Kowalska",
        date(2020, 5, 1),
        date(1990, 3, 12),
        "Warsaw",
        "Green 3",
        "00-002",
        "111111111",
    ),
    Employee(
        "Piotr",
        "Nowak",
        date(2019, 3, 15),
        date(1988, 7, 22),
        "Krakow",
        "Blue 7",
        "30-002",
        "222222222",
    ),
    Employee(
        "Maria",
        "Wisniewska",
        date(2021, 10, 10),
        date(1995, 1, 5),
        "Warsaw",
        "Red 9",
        "00-003",
        "333333333",
    ),
]

students = [
    Student("Jan", "Kaczmarek", "S001", "444444444"),
    Student("Alicja", "Lewandowska", "S002", "555555555"),
    Student("Tomasz", "Zielinski", "S003", "666666666"),
]

books = [
    Book(library1, date(2010, 6, 1), "Adam", "Mickiewicz", 320),
    Book(library1, date(2015, 4, 12), "Henryk", "Sienkiewicz", 450),
    Book(library2, date(2005, 9, 20), "Boleslaw", "Prus", 380),
    Book(library2, date(2020, 1, 5), "Olga", "Tokarczuk", 290),
    Book(library1, date(2018, 11, 30), "Stanislaw", "Lem", 410),
]

order1 = Order(employees[0], students[0], books[:3], date.today())
order2 = Order(employees[1], students[1], books[3:], date.today())

# =========================
# Wyświetlenie zamówień
# =========================

print(order1)
print("\n" + "=" * 80 + "\n")
print(order2)
