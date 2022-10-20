days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}

lista=[]
for v in days.values():
    print(v)
    #if lista.count(v) == 0:
    if v not in lista:
        lista.append(v)
    print(lista)


