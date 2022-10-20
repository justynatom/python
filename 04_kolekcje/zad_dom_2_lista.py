tablica_liczb = []
for liczba in range(10):
    liczba=int(input("Podaj liczbę: "))
    tablica_liczb.append(liczba)
    print(liczba)


print(tablica_liczb)

for liczba in tablica_liczb:
    if liczba%2==0:
        print(liczba)

