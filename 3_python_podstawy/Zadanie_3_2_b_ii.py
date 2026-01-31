# 2.b. Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych liczb, każdy jej element pomnoży przez 2, a na końcu ją zwróci. Zadanie należy wykonać w 2 wersjach:
# ii. Wykorzystując listę składaną.


def podwoj_liczby_lc(liczby):
    return [liczba * 2 for liczba in liczby]


lista = [1, 3, 5, 7, 9]
print(podwoj_liczby_lc(lista))
