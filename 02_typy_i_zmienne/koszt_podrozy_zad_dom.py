dystans=int(input("Podaj dystans trasy w km: "))
spalanie_100=float(input("Podaj wartość spalania: "))
benzyna=float(input("Podaj cenę benzyny za 1l: "))

result=benzyna*dystans/100*spalanie_100
print(result)

print("Cena całkowita trasy 120km:", round(result,2), 'zł')