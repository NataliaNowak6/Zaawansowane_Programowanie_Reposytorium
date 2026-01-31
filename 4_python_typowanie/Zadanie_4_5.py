# Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi typu int . Funkcja ma sprawdzić (zwracając typ logiczny bool ),
# czy lista z parametru pierwszego zawiera taką wartość jaką przekazano w parametrze drugim.

from typing import List


def contains_value(values: List[int], target: int) -> bool:
    return target in values


if __name__ == "__main__":
    nums: List[int] = [1, 5, 8, 10]
    print(contains_value(nums, 8))  # True
    print(contains_value(nums, 7))  # False
