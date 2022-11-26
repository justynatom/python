def check_values(*values):
    print(values)
    for item in values:
        if not isinstance(item, (int, float)):
            print('-->', item)
            raise ValueError("Bok musi być wartością numeryczną")


def square_area(a):
    check_values(a)
    # if not isinstance(a, (int, float)):
    #     raise ValueError("Bok musi być wartością numeryczną")
    return a * a
   # except TypeError as err:
     #   print(err,'->', side)

def rectangle_area(a, b):
    check_values(a, b)
    # if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    #     raise ValueError("Bok musi być wartością numeryczną")
    return a*b


def triangle_area(a, b):
    check_values(a, b)
    # if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    #     raise ValueError("Bok musi być wartością numeryczną")
    return a * b * 0.5

def trapezoid_area(a, b, h):
    check_values(a, b, h)
    # if not isinstance(a, (int, float))\
    #         or not isinstance(b, (int, float))\
    #         or not isinstance(h, (int, float)) :
    #     raise ValueError("Boki i wysokość muszą być wartością numeryczną")
    return (a+b)*0.5*h

def main():
    result_s = square_area('lalala')
    print(result_s == 25)

    result_r = rectangle_area(5, 'b')
    print(result_r == 30)
    print(result_r != 36)

if __name__ =='__main__':
    main()