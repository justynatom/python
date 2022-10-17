slowo="cokolwiekabra"

if len(slowo)>5:
    print("Ciąg znaków jest dłuższy niz 5 znaków.")
else:
    print("Ciąg znaków jest krótszy niż 5 znaków")
if "a" in slowo:
    print("Znalazlo szukaną litere w slowie")
    slowo=slowo.replace('a', 'z')
else:
    print("Nie ma szukanej litery w słowie")

print(slowo)