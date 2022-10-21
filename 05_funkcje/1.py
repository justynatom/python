def add_book():
    title=input("podaj tytul ksiazki: ")
    rate=int(input("podaj ocene ksiazki: "))
    list_book.append([title, rate])

list_book=[]
for i in range(3):
    print("ksiazka", i +1)
    add_book()
print(list_book)


# def numer_ksiazki():
#     numer=int(input("podaj numer ksiazki: "))
#     if 1>numer or numer>3:
#          print("numer nie istnieje")
#     else:
#         print("tytul: ", list_book[numer-1][0],"ocena:",  list_book[numer-1][1])
#
def numer_ksiazki():
    while True:
        numer=int(input("podaj numer ksiazki: "))
        if 3>=numer>=1 :
            print("tytul: ", list_book[numer-1][0],"ocena:",  list_book[numer-1][1])
            break
        else:
            print("numer nie istnieje")


numer_ksiazki()


# def dodaj_ksiazke():
#     ksiazka=input("Podaj tytuł ksiązki: ")
#
# def dadaj_ocene():
#     ocena = int(input("podaj ocene ksiazki: "))
#     return
#
# tablica=[]
# dodaj_ksiazke()
# tablica.append(dodaj_ksiazke())

