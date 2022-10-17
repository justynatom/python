slowo=input("Podaj slowo: ")
print(slowo)
print("wyświetlenie parzystych znakow w słowie: ",slowo[0: :2])

print("długość słowa: ",len(slowo))

litera=""
for index in range(0,len(slowo),2):
    print(index, slowo[index])
    litera=litera+slowo[index]
print(litera)


