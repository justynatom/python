# user_value = input("Podaj liczbę od 1 do 100: ")
# print(user_value.isdecimal())
# while True:
#     if user_value.isdecimal() == False:
#         print("błąd składni.")
#         user_value = input("Podaj liczbę jeszcze raz: ")
#
#     user_value = int(user_value)
#
#     number = user_value / 4
#     print(f" Number = { number }")


# while True:

def get_calculation():
    try:
        num = int(input("podaj cyfre: "))
        x = 5 / num
    except ZeroDivisionError:
        raise ValueError
    return x

def main():
    try:
        get_calculation()
    except ValueError as err:
        print("wystapil blad wartosci")
        # print("pamietaj kolego nie dziel przez zero")
        print(err)
    finally:
        print("hello")

    print("bye bye")
    # except ValueError:
    #     print("wystapil blad. ten string nie jest liczba")
    print("hello!!! :D ")

if __name__ == "__main__":
    main()