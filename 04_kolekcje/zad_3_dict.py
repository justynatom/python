n=int(input("Podaj liczbe 1-10: "))
a = [["-"] * n] * n

# for i in a:
#     print(' '.join(i))
#
for i in a:
    for col in i:
        print(col, end=" ")
    print()
