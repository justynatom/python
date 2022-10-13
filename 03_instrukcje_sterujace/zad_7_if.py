masa=int(input("podaj swoja mase ciala[kg]: "))
wzrost=float(input("podaj swoj wzrost[m]: "))
Bmi=((masa)/(wzrost)**2)
Bmi=round(Bmi, 2)
print(Bmi)

if Bmi<18:
    print("niedowaga")
elif Bmi<=25:
    print("w normie")
elif Bmi<=30:
    print("nadwaga")
else:
    print("otylosc")