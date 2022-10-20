liczba=(2,5,2,1,5,6,2,9,1)
tablica=[]

for i in liczba:
    print("liczba: ",i," występuje: ",liczba.count(i))
    if liczba.count(i)>=2:
        tablica.append(i)
    print(tablica)