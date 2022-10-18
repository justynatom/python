krotka1=(1,2,4,2,1,2,4,1)
krotka2=("a","b","a","c","b","c","b","a")

print(krotka2[::2])
print(krotka1[1::2])

nowa_lista= list(krotka2[::2]+krotka1[1::2])
print(nowa_lista)

print(set(nowa_lista))

