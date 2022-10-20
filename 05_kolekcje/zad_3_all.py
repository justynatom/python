lista=[]
# def porownanie():
#     for i in range(3):
#         liczba=int(input("Podaj liczbe:"))
#         lista.append(liczba)
#         print(lista)
#         for index in lista:
#             if index<index+1:
#                 max_liczba=index
#                 print(max_liczba)
#
#
# porownanie()

def maximum_of(a,b,c):
    najwieksza=0
    if a>b and a>c:
        najwieksza=a
    elif b>a and b>c:
        najwieksza=b
    else:
        najwieksza=c
    return najwieksza

a=int(input("Podaj liczbe:"))
b=int(input("Podaj liczbe:"))
c=int(input("Podaj liczbe:"))

print(maximum_of(a,b,c))
maximum_of(a,b,c)

# def max_of_2(x,y):
#     if x>y:
#         return x
#     else:
#         return y
