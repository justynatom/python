def suma_numbers(lista_liczb):
    suma=0
    for i in lista_liczb:
        suma+=i
    return suma
    # for i in liczba():
    #     podaj_liczbe=input("podaj liczbe: ")
    #     lista_liczb.append(podaj_liczbe)
    #     print(lista_liczb)

num=[1,2,3,4]
wynik=suma_numbers(num)
print(f"Suma z {num} to jest {wynik}")
