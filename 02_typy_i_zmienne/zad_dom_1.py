wyraz='abracadabra'
dlugosc= len(wyraz)
index_srodek=dlugosc//2
index_poprzedni= index_srodek-1
index_nastepny=index_srodek+1
print(wyraz[index_poprzedni]+wyraz[index_srodek]+wyraz[index_nastepny])
#print(wyraz[4:7])
print(wyraz[index_poprzedni:index_nastepny+1])




