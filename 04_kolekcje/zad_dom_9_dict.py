tablica_przedmiotow=[]
for numer_uzytkownika in range(1,6):
    for numer_przedmiotu in range(1,5):
        print("numer_uzytkownika: ",numer_uzytkownika, "numer_przedmiotu: ", numer_przedmiotu)
        przedmiot=input("podaj nazwę przedmiotu szkolnych: ")
        przedmiot=przedmiot.lower()
        tablica_przedmiotow.append(przedmiot)
        print("przedmiot o nazwie:", przedmiot, " występuje: ",tablica_przedmiotow.count(przedmiot))

#tablica_przedmiotow=['wf', 'rel', 'ang', 'wf', 'pol', 'wf', 'ang', 'ang', 'pol', 'fiz']
print(tablica_przedmiotow)
max_ilosc_wystapien=0
najpopularniejszy_przedmiot=""

for przedmiot in tablica_przedmiotow:
    ilosc_wystapien=tablica_przedmiotow.count(przedmiot)
    print("ilosc wystapien: ",ilosc_wystapien, "przedmiotu: ", przedmiot)
    if max_ilosc_wystapien >ilosc_wystapien:
        max_ilosc_wystapien = max_ilosc_wystapien
    else:
        max_ilosc_wystapien=ilosc_wystapien
        najpopularniejszy_przedmiot = przedmiot
print("Najpopularniejszym przedmiotem jest: ", najpopularniejszy_przedmiot)



# print("i: ", end=' ')
# for i in range(10):
#     #i = 0, 1, 2, 3, 4 ... 9
#     print(i, end=' ')
#
# print()
# print("j: ", end=' ')
# for j in range(1, 10):
#     #j = 1, 2, 3, 4 .. 9
#     print(j, end=' ')
#
# print()
# print("k: ", end=' ')
# for k in range(0, 100, 10):
#     #k = 0, 10, 20, 30 ... 90
#     print(k, end=' ')
#
# print()
# print("zwierze: ", end=' ')
# for zwierze in ['kot', 'pies', 'lis'] :
#     #zwierze = 'kot', 'pies', 'lis'
#     print(zwierze, end=' ')
#
# lista = ['slon', 'lew', 'tygrys']
#
# print()
# print("m: ", end=' ')
# for m in lista:
#     #m = 'slon', 'lew', 'tygrys'
#     print(m, end=' ')
#
# print()
# print("n: ", end=' ')
# for n in range(len(lista)):
#     #n = 1, 2, 3
#     print(n, end=' ')
#
# print()
# print("v: ", end=' ')
# dlugosc=15
# for v in range(dlugosc):
#     #v = 15
#     print(v, end=' ')
#
# zagniezdzona_lista = [['slon', 'lew', 'tygrys'], ['kot', 'pies', 'lis'], 'kolo', ['ala', 'ola', 'ela']]
#
# print()
# for b in zagniezdzona_lista:
#     # b = ['slon', 'lew', 'tygrys'], ['kot', 'pies', 'lis'], 'kolo', ['ala', 'ola', 'ela']
#     print()
#     print("b: ", end=' ')
#     print(b)
#     print("d: ", end=' ')
#     for d in b:
#         # d = 0, 1, 2, 3
#         print(d, end=' ')