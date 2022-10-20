liczba=0
lista=[]
while liczba != "":
    liczba=input("Podaj liczbę: ")
    if liczba.isdecimal():
        lista.append(int(liczba))
    print("długośc listy: ", len(lista),", lista= ", lista)
    if len(lista)%2 != 0:
        print("Podaj kolejną liczbę ")
    else:
        print("Podaj kolejną liczbę lub zakończ wprwdzanie liczb wpisująć pusty znak2 ")


# len(lista)/2 == (len(lista)/2)-1:
if lista[len(lista)//2] == lista[len(lista)//2-1]:
    print("2 środkowe elementy są takie same")
else:
    print("2 środkowe elementy są różne")