# Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu list .
# Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć duplikaty, każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić powstałą listę.

from typing import List


def merge_unique_and_cube(a: List[int], b: List[int]) -> List[int]:
    merged_unique = set(a) | set(b)  # łączenie + usuwanie duplikatów
    result = [x**3 for x in merged_unique]  # potęga 3
    return result


if __name__ == "__main__":
    l1 = [1, 2, 2, 3]
    l2 = [3, 4, 5]
    print(merge_unique_and_cube(l1, l2))
