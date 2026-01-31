# Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma dwóch pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę informację jako typ logiczny bool


def sum_first_two_ge_third(a: int, b: int, c: int) -> bool:
    return (a + b) >= c


if __name__ == "__main__":
    print(sum_first_two_ge_third(3, 5, 8))  # True
    print(sum_first_two_ge_third(3, 4, 8))  # False
