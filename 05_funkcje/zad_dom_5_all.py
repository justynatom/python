import random

def wylosuj_liczbe():
    liczba_komputera=random.randint(1,100)
    return liczba_komputera

def pobierz_liczbe_od_uzytkownika():
    liczba_uzytkownika=int(input("Podaj liczbę: "))
    return liczba_uzytkownika

def wyswietl_cieplo_zimno_i_zwroc_poprzednia_liczbe_uzytk(liczba_uzytkownika, liczba_komputera, poprzednia_liczba_uzytkownika):
    if liczba_uzytkownika == liczba_komputera:
        print("Brawo! Liczba została odgadnięta.")
    elif abs(liczba_komputera-liczba_uzytkownika) < abs(liczba_komputera-poprzednia_liczba_uzytkownika):
        print("Ciepło.")
    else:
        print("Zimno.")
    poprzednia_liczba_uzytkownika=liczba_uzytkownika
    return poprzednia_liczba_uzytkownika

def pobierz_liczbe_od_uzytkownika_i_wyswietl_efekt(liczba_komputera, poprzednia_liczba_uzytkownika):
    liczba_uzytk = pobierz_liczbe_od_uzytkownika()
    poprzednia_liczba_uzytkownika=wyswietl_cieplo_zimno_i_zwroc_poprzednia_liczbe_uzytk(liczba_uzytk, liczba_komputera, poprzednia_liczba_uzytkownika)
    return poprzednia_liczba_uzytkownika

def wyswietl_kto_wygral(poprzednia_liczba_uzytkownika, liczba_komp):
    if poprzednia_liczba_uzytkownika == liczba_komp:
        print("Brawo! Liczba odgadnięta. Pokonałeś komputer.")
    else:
        print("Niestety, nie udało Ci się wygrać. Wygrywa komputer.")

def czy_liczba_odgadnieta(poprzednia_liczba_uzytkownika, liczba_komp):
    prawda_czy_falsz= poprzednia_liczba_uzytkownika == liczba_komp
    return prawda_czy_falsz



liczba_komp = wylosuj_liczbe()
print(liczba_komp)
poprzednia_liczba_uzytkownika= -200

liczba_prob = 6
for i in range(liczba_prob):
    if not czy_liczba_odgadnieta(poprzednia_liczba_uzytkownika, liczba_komp):
    #if poprzednia_liczba_uzytkownika != liczba_komp:
        poprzednia_liczba_uzytkownika = pobierz_liczbe_od_uzytkownika_i_wyswietl_efekt(liczba_komp, poprzednia_liczba_uzytkownika)
    # if poprzednia_liczba_uzytkownika != liczba_komp:
    #     break
wyswietl_kto_wygral(poprzednia_liczba_uzytkownika, liczba_komp)



