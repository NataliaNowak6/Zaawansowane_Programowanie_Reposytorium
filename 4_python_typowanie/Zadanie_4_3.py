# Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w parametrze jest parzysta i zwróci tą informację jako typ logiczny bool ( True / False ).
# Należy uruchomić funkcję, wynik wykonania zapisać do zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy tekst "Liczba parzysta" / "Liczba nieparzysta"


def is_even(n: int) -> bool:
    return n % 2 == 0


if __name__ == "__main__":
    number: int = 13
    even_result: bool = is_even(number)

    if even_result:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")
