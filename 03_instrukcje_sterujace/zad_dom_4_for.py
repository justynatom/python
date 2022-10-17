silnia=1
liczba=int(input("Podaj liczbę: "))
if liczba <= 8:
    for liczba in range(1,liczba+1):
        print("Podana liczba:" ,liczba)
        silnia=silnia*liczba
        print("Wynik silnia " + str(liczba) + "!: " + str(silnia))
else:
    print("Podana liczba nie może być większa niż 8.")