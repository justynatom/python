import random

wybor_figur=["k","p","n"]
liczba_rund=int(input("Ile rund chcesz rozegrać? : "))

pkt_uzyt = 0
pkt_komp = 0
for i in range(liczba_rund):
    wybor_uzytkownika=input("Wybierz figurę \n -k (kamień)\n -p (papier)\n -n (nożyce): ")
    wybor_komp=random.choice(wybor_figur)

    print("wybrałes figurę: ", wybor_uzytkownika)
    print("Komputer wybrał: ", wybor_komp)

    if wybor_uzytkownika =="k" and wybor_komp  =="k":
        pkt_uzyt = 0
        pkt_komp = 0
        print("Remis. Liczba punktów dla obu graczy bez zmian.")
    elif wybor_uzytkownika == "p" and wybor_komp == "p":
        pkt_uzyt = 0
        pkt_komp = 0
        print("Remis. Liczba punktów dla obu graczy bez zmian.")
    elif wybor_uzytkownika == "n" and wybor_komp == "n":
        pkt_uzyt = 0
        pkt_komp = 0
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
    print("Suma pkt uzytkownika: ", pkt_uzyt, "Suma pkt komputera: ", pkt_komp)

if pkt_uzyt > pkt_komp:
    print("Wygrał użytkownik!")
elif pkt_komp == pkt_uzyt:
    print("Remis.")
else:
    print("Wygrał komputer.")







# from random import randint
# kamien="k"
# papier="p"
# nozyce="n"
# pkt_uz=0
# pkt_kom=0
#
# uz=input("Wybierz kamien 'k', papier 'p' lub nożyce 'c': ")
# kom=randint(1,3)
#
# if uz=="k" and kom=="k":
#     pkt_uz= 0, pkt_kom= 0
# elif uz=="p" and kom=="p":
#     pkt_uz = 0, pkt_kom = 0
# elif uz=="n" and kom=="n":
#     pkt_uz = 0, pkt_kom = 0
# elif uz=="k" and kom=="p":
#     pkt_uz = 0, pkt_kom = pkt_kom+1
# elif uz=="k" and kom=="n":
#     pkt_uz = pkt_uz+1, pkt_kom = 0
# elif uz=="p" and kom=="k":
#     pkt_uz = pkt_uz+1, pkt_kom = 0
# elif uz=="p" and kom=="n":
#     pkt_uz = 0, pkt_kom = pkt_kom+1
# elif uz=="n" and kom=="k":
#     pkt_uz = 0, pkt_kom = pkt_kom+1
# elif uz=="n" and kom=="p":
#     pkt_uz = pkt_uz+1, pkt_kom = 0
#
# if pkt_uz > pkt_kom:
#     print("Wygrywa użytkownik")
# elif pkt_uz == pkt_kom:
#     print("Remis")
# else:
#     print("wygrywa komputer")