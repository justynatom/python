# #zad.1
# wyraz='abracadabra'
# dlugosc= len(wyraz)
# index_srodek=dlugosc//2
# index_poprzedni= index_srodek-1
# index_nastepny=index_srodek+1
# print(wyraz[index_poprzedni]+wyraz[index_srodek]+wyraz[index_nastepny])
# #print(wyraz[4:7])
# print(wyraz[index_poprzedni:index_nastepny+1])
#
# #zad.2
# s1='banana'
# s2="dom"
# s3=s1[:3]+s2+s1[3:]
# print(s3)

#zad.3
# quote="Honesty is the first chapter in the book of wisdom."
# dlugosc=len(quote)
# print("1",dlugosc)
# print('2',quote[-7:-1])
# print('3',quote[:len(quote)//2])
# print('4',quote[-1])
# print('5',quote[len(quote)//2::3])
# print('6',quote[: :2])
# print('7',quote[: :-1])
# print('8',quote.replace('wisdom', 'friendship'))

#zad5
# palindrom=input("Podaj dowolne zdanie,aby sprawdzic czy jest palindromem: ")
# if palindrom[::]==palindrom[::-1]:
#     print("twoje zdanie jest palidromem.")
# else:
#     print("twoje zdanie nie jest palidromem")

text=input("podaj zdanie: ")
text=text.replace(" ","")
text.lower()
print('jest palidrom-> ', text==text[::-1])


# palindrom = input("Podaj dowolne zdanie,aby sprawdzic czy jest palindromem: ")
# if palindrom[::] == palindrom[::-1]:
#     print("twoje zdanie jest palidromem.")
# else:
#     print("twoje zdanie nie jest palidromem")
