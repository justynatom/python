example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

tablica=[]
for i in example_list:
    print("i: ", i, "tablica.count(i): ", tablica.count(i))
    if tablica.count(i) < 1:
        print('if')
        tablica.append(i)
    else:
        print('else')
        tablica.remove(i)
    print(tablica)

print("minimalba wartość w tablicy:", min(tablica))
print("maksymalna wartość w tablicy: ", max(tablica))