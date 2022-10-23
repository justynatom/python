import random

def wyswietl_koncowe_wyniki(pkt_uzyt, pkt_komp):
    if pkt_uzyt > pkt_komp:
        print("Wynik końcowy: wygrał użytkownik!")
    elif pkt_komp == pkt_uzyt:
        print("Wynik końcowy: remis.")
    else:
        print("Wynik końcowy: wygrał komputer.")

def wybieranie_figur():
    wybor_figur=["k","p","n"]
    wybor_komp = random.choice(wybor_figur)
    return wybor_komp

def sprawdz_kto_wygral(pkt_uzyt, pkt_komp, wybor_uzytkownika, wybor_komp):
    if wybor_uzytkownika =="k" and wybor_komp  =="k":
        pkt_uzyt += 0
        pkt_komp += 0
        print("Remis. Liczba punktów dla obu graczy bez zmian.")
    elif wybor_uzytkownika == "p" and wybor_komp == "p":
        pkt_uzyt += 0
        pkt_komp += 0
        print("Remis. Liczba punktów dla obu graczy bez zmian.")
    elif wybor_uzytkownika == "n" and wybor_komp == "n":
        pkt_uzyt += 0
        pkt_komp += 0
        print("Remis. Liczba punktów dla obu graczy bez zmian.")
    elif wybor_uzytkownika == "k" and wybor_komp == "p":
        pkt_uzyt += 0
        pkt_komp += 1
        print("Punkt dla komputera.")
    elif wybor_uzytkownika == "k" and wybor_komp == "n":
        pkt_uzyt += 1
        pkt_komp += 0
        print("Punkt dla użytkownika.")
    elif wybor_uzytkownika == "p" and wybor_komp == "k":
        pkt_uzyt += 1
        pkt_komp += 0
        print("Punkt dla użytkownika.")
    elif wybor_uzytkownika == "p" and wybor_komp == "n":
        pkt_uzyt += 0
        pkt_komp += 1
        print("Punkt dla komputera.")
    elif wybor_uzytkownika == "n" and wybor_komp == "p":
        pkt_uzyt += 1
        pkt_komp += 0
        print("Punkt dla użytkownika.")
    elif wybor_uzytkownika == "n" and wybor_komp == "k":
        pkt_uzyt += 0
        pkt_komp += 1
        print("Punkt dla komputera.")
    return pkt_komp, pkt_uzyt




liczba_rund=int(input("Ile rund chcesz rozegrać? : "))

pkt_uzyt = 0
pkt_komp = 0
for i in range(liczba_rund):
    wybor_uzytkownika=input("Wybierz figurę \n -k (kamień)\n -p (papier)\n -n (nożyce): ")
    wybor_komp = wybieranie_figur()
    print("wybrałes figurę: ", wybor_uzytkownika)
    print("Komputer wybrał: ", wybor_komp)
    pkt_komp, pkt_uzyt = sprawdz_kto_wygral(pkt_uzyt, pkt_komp, wybor_uzytkownika, wybor_komp)
    print("Suma pkt uzytkownika: ", pkt_uzyt, "Suma pkt komputera: ", pkt_komp)


wyswietl_koncowe_wyniki(pkt_uzyt, pkt_komp)



