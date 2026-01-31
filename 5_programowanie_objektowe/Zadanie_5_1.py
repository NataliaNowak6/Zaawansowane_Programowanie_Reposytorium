# Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną metodę is_passed,
# która zwraca wartość logiczną, pozytywną gdy średnia ocen jest > 50 w przeciwnym przypadku negatywną.
# Następnie należy stworzyć 2 przykładowe obiekty klasy, tak aby dla pierwszego obiektu metoda zwracała true , a dla drugiego false .

from typing import List


class Student:
    def __init__(self, name: str, marks: List[int]):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        average = sum(self.marks) / len(self.marks)
        return average > 50

    def __str__(self) -> str:
        return f"Student: {self.name}, średnia: {sum(self.marks)/len(self.marks):.2f}"


student_passed = Student("Jan Kowalski", [60, 70, 80])
student_failed = Student("Anna Nowak", [30, 40, 50])

print(student_passed, "->", student_passed.is_passed())
print(student_failed, "->", student_failed.is_passed())
