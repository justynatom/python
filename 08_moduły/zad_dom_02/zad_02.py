import math

def get_parameters_delta():
    a = int(input("Podaj wartość a: "))
    b = int(input("Podaj wartość b: "))
    c = int(input("Podaj wartość c: "))
    return a, b, c


def calculate_delta(a, b, c):
    delta = pow(b,2) - 4*a*c
    return delta

def main():
    d, e, f = get_parameters_delta()
    result = calculate_delta(d, e, f)
    print(result)


if __name__ == "__main__":
    main()





#wzor_delta = b^2-4*a*c
