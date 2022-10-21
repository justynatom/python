def kalkulator_bmi():
    masa = int(input("podaj swoja mase ciala[kg]: "))
    wzrost = float(input("podaj swoj wzrost[m]: "))
    Bmi = ((masa) / (wzrost) ** 2)
    Bmi = round(Bmi, 2)
    print(Bmi)
    return Bmi

def przedzial_bmi(Bmi_value):
    if Bmi_value < 18:
        return "niedowaga"
    elif Bmi_value <= 25:
        return "w normie"
    elif Bmi_value <= 30:
        return "nadwaga"
    else:
        return "otylosc"

wynik_bmi=kalkulator_bmi()
status= przedzial_bmi(wynik_bmi)
print(status)