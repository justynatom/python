liczba=(2,5,6,7,9,12,14)
liczba_uzytkownika=int(input("Podaj liczbę: "))

# for index in range(len(liczba)):
#     if liczba[index]== liczba_uzytkownika:
#         print("Index: ", index)

# for index, value in enumerate(liczba):
#     print(index, value)
#     if value==liczba_uzytkownika:
#         print("Index: ", index)

print(f" numer {liczba_uzytkownika} w krotce { liczba_uzytkownika in liczba}")
print(f" numer {liczba_uzytkownika} jest o indeksie {liczba.index(liczba_uzytkownika)}")