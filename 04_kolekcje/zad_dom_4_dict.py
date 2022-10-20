n=10
a = [['-'] * n] * n
print(a)

a[1][3]=4
print(a)

tablica=[]

for i in range(n):
    tablica1=[]
    for j in range(n):
        tablica1.append(j)
    tablica.append(tablica1)


for i in range(n):
    tablica[i][0]=i

for i in range(1,n):
    for j in range(1,n):
        tablica[i][j]=tablica[i][0]*tablica[0][j]

for i in tablica:
    for col in i:
        print(col, '\t',  end="")
    print()

