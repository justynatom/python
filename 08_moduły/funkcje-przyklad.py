# def wypisani():
#     print("ala ma kota")
#
# wypisani()
#
# def obliczanie(a, b):
#     print("1: ", a, b)
#     print(a+b)
#
#
# a = 10
# b = 5
# obliczanie(a, b)
#
# obliczanie(8, 4)
# print(a, b)
#
#
# pierwsza = 30
# druga = 2
# obliczanie(pierwsza, druga)
#
# def dodawanie_wzracanie(a, b):
#     suma = a+b
#     return suma
#
# c = 6
# d= 1
# dodawanie_wzracanie(c, d)
# print(dodawanie_wzracanie(c, d))
#
# moja_suma = dodawanie_wzracanie(c,d)
# print(moja_suma)
# tab=[]
# for i in range(1,11):
#     j = i*i
#     tab.append(j)
# print(tab)

def kwadrat(a):
    liczba = a
    kwadrat_liczby = liczba * liczba
    # wynik = kwadrat_liczby * kwadrat_liczby
    # print(kwadrat_liczby, wynik)
    return kwadrat_liczby

wynik = kwadrat(a=3)
print(wynik)

b=4
print(b, kwadrat(b))
