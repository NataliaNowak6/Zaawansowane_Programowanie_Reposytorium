from datetime import date
from typing import List
from Classes.Library import Library


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: date, birth_date: date,
                 city: str, street: str, zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return f"Employee: {self.first_name} {self.last_name}"


class Student:
    def __init__(self, first_name: str, last_name: str, student_id: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.phone = phone

    def __str__(self) -> str:
        return f"Student: {self.first_name} {self.last_name}"


class Book:
    def __init__(self, library: Library, publication_date: date, author_name: str,
                 author_surname: str, number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f"Book by {self.author_name} {self.author_surname} in {self.library}"


class Order:
    def __init__(self, employee: Employee, student: Student, books: List[Book], order_date: date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        books_str = "\n".join(str(book) for book in self.books)
        return f"Order on {self.order_date}\n{self.employee}\n{self.student}\nBooks:\n{books_str}"