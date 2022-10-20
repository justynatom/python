from random import randint
kamien="k"
papier="p"
nozyce="n"
pkt_uz=0
pkt_kom=0

uz=input("Wybierz kamien 'k', papier 'p' lub nożyce 'c': ")
kom=randint(1,3)

if uz=="k" and kom=="k":
    pkt_uz= 0, pkt_kom= 0
elif uz=="p" and kom=="p":
    pkt_uz = 0, pkt_kom = 0
elif uz=="n" and kom=="n":
    pkt_uz = 0, pkt_kom = 0
elif uz=="k" and kom=="p":
    pkt_uz = 0, pkt_kom = pkt_kom+1
elif uz=="k" and kom=="n":
    pkt_uz = pkt_uz+1, pkt_kom = 0
elif uz=="p" and kom=="k":
    pkt_uz = pkt_uz+1, pkt_kom = 0
elif uz=="p" and kom=="n":
    pkt_uz = 0, pkt_kom = pkt_kom+1
elif uz=="n" and kom=="k":
    pkt_uz = 0, pkt_kom = pkt_kom+1
elif uz=="n" and kom=="p":
    pkt_uz = pkt_uz+1, pkt_kom = 0

if pkt_uz > pkt_kom:
    print("Wygrywa użytkownik")
elif pkt_uz == pkt_kom:
    print("Remis")
else:
    print("wygrywa komputer")