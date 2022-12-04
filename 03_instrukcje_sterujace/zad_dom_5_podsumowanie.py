import random

liczba_komputera=random.randint(1, 100)
poprzednia_liczba_uzytkownika = -100
for i in range(6):
    liczba_uzytkownika=int(input("Podaj liczbę: "))
    #poprzednia_liczba_uzytkownika = liczba_uzytkownika

    if liczba_uzytkownika == liczba_komputera:
        print("Brawo! Liczba została odgadnięta.")
        pass
    elif abs(liczba_komputera-liczba_uzytkownika) < abs(liczba_komputera-poprzednia_liczba_uzytkownika):
        print("Ciepło.")
    else:
        print("Zimno.")
    poprzednia_liczba_uzytkownika=liczba_uzytkownika

if poprzednia_liczba_uzytkownika == liczba_komputera:
    print("Brawo! Liczba odgadnięta. Pokonałeś komputer.")
else:
    print("Niestety, nie udało Ci się wygrać. Wygrywa komputer.")


prawda_czy_falsz = poprzednia_liczba_uzytkownika == liczba_komputera

print(liczba_komputera)
poprzednia_liczba_uzytkownika= -200

