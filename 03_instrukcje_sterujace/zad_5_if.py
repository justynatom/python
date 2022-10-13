password=input("podaj haslo:")

if len(password)<8 or len(password)>24:
    print("hasło jest nieprawidlowe")
if password.isdigit():
    print("hasło musi zawierac litery")
if password.isalpha():
    print("haslo powinno zaweirac cyfry")
if password.islower():
    print("haslo zawiera tylko male litery, a powinno zaweirac 1 duza")
if password.isupper():
    print("haslo zawiera tylko duze litery, a powinno miec conajmniej 1 mala")


else:
    print("haslo jest odpowiednie")



#password.isalnum()