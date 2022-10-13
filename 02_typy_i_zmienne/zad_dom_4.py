tytul_ksiazki=input("Podaj tytuł książki: ")
autor=input("Podaj nazwisko autora książki: ")
strony=input("Podaj liczbę stron kiążki: ")

print("Czy tytuł książki składa się tylko z liter?",tytul_ksiazki.isalpha())
print("Czy nazwisko autora książki składa się tylko z liter?",autor.isalpha())
print("Czy ilość stron książki jest wartością liczbową?",strony.isdecimal())

print(tytul_ksiazki.capitalize(), autor.capitalize())

book=tytul_ksiazki+" "+autor+" "+strony
print(book)
print("liczba wszystkich znakow w zmiennej 'book'wynosi: ", len(book))
book_join=" ".join([tytul_ksiazki,autor,strony])
print("funkcja join:", book_join)