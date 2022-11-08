items = [0, 13, 'string', 2.45, 0, {}, True, False, [], (), {'key': 'klucz'}]

index=int(input("Podaj wartosc indeksu: "))

# for index in items:
try:
    x = 1/items[index]
    print(x)
except TypeError:
    print("blad typu")
except ZeroDivisionError:
    print("nie dziel przez zero")
except IndexError:
     print("wyszliśmy poza zakres")
except ValueError:
    print("błędna wartość")
