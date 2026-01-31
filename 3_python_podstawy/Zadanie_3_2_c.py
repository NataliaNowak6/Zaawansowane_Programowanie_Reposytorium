# Utwórz funkcję, która otrzyma w parametrze listę 10 liczb (rekomendowane wykorzystanie funkcji range ),
# a następnie wyświetli Interpreter python, podstawowe operacje (zmienne, warunku, pętle, funkcje) 11 jedynie parzyste elementy.


def wyswietl_parzyste(liczby):
    for liczba in liczby:
        if liczba % 2 == 0:
            print(liczba)


lista_liczb = list(range(10))
wyswietl_parzyste(lista_liczb)
