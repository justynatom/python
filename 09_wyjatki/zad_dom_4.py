
#arithmetic_average

def get_numbers():
    numbers = input("Podaj kilka liczb wypisanych po przecinku: ")
    print(numbers)
    convert_numbers = tuple(map(int, numbers.split(', ')))
    print(convert_numbers)
    return convert_numbers

def aritmetic_average(numbers):
    sum_numbers = 0
    for i in numbers:
        sum_numbers = sum_numbers + i
    aritmetic_average = sum_numbers / len(numbers)
    print(aritmetic_average)
    return aritmetic_average

try:
    get_numbers()
except ValueError as e:
    print(e)
    with open("bledy.txt", "a") as f:
        f.write(str(e)+"\n")




aritmetic_average(get_numbers())

