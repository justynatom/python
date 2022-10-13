ocena=int(input("Podaj ocene ksiązki: "))
ocena2=int(input("Podaj ocene ksiązki: "))
ocena3=int(input("Podaj ocene ksiązki: "))

ocena_srednia=(ocena3+ocena2+ocena)/3

if ocena>7:
    print("bardzo dobra")
elif ocena>=5:
    print("przecietna")
else:
    print("nie warta uwagi")