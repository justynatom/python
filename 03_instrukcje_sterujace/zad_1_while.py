#temperatura=int(input("podaj temperature w F"))

# fahr=0
# while fahr<=200:
#     Celc=((fahr-32)*(5/9))
#     Celc=round(Celc,2)
#     print(f"{fahr} st Fahrenhaita-> {Celc} st C-")
#     fahr=fahr+20

for fahre in range (0,201,20):
    Celc = ((fahre - 32) * (5 / 9))
    Celc=round(Celc,2)
    print(f"{fahre} st Fahrenhaita-> {Celc} st C-")