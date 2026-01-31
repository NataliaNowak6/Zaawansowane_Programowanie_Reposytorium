# Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych liczb, każdy jej element pomnoży przez 2, a na końcu ją zwróci. Zadanie należy wykonać w 2 wersjach:
# i. Wykorzystując pętle for


def podwoj_liczby_for(liczby):
    wynik = []
    for liczba in liczby:
        wynik.append(liczba * 2)
    return wynik


lista = [1, 3, 5, 7, 9]
print(podwoj_liczby_for(lista))
