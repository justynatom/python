def min_of(a,b,c):
    najmniejsza=0
    if a < b and a < c:
        najmniejsza=a
    elif b < a and b < c:
        najmniejsza=b
    else:
        najmniejsza=c
    return najmniejsza
a=int(input("Podaj liczbę: "))
b=int(input("Podaj liczbę: "))
c=int(input("Podaj liczbę: "))

min_of(a,b,c)
print("Najmniejszą wartością jest:", min_of(a,b,c))
