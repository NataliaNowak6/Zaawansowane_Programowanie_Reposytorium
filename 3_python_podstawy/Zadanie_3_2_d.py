# Utwórz funkcję, która otrzyma w parametrze listę 10 liczb (rekomendowane wykorzystanie funkcji range ), a następnie wyświetli co drugi element.


def wyswietl_co_drugi(liczby):
    for i in range(0, len(liczby), 2):
        print(liczby[i])


lista_liczb = list(range(10))
wyswietl_co_drugi(lista_liczb)
