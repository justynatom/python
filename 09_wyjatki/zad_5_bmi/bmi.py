def get_safe_value(message):
    while True:
        try:
            value = float(input(message))
            break
        except ValueError as err:
            print("bląd typu ", err)


    return value

def get_posible_value(message, ):
    while True:
        h = float(input('Height[m]:'))
        if 2.3 <= h or h <= 1.4:
            print("this is imposible value")
        else:
            break

def get_user_params():
    while True:
        h = float(input('Height[m]:'))
        if 2.3 <= h or h <= 1.4:
            print("this is imposible value")
        else:
            break

    while True:
        w = float(input("Weight[kg]: "))
        if 20 > w or w > 200:
            print("this is imposible value")
        return h, w

def calculate_bmi(h, w):
    bmi = w / (h ** 2)
    print('BMI result:', round(bmi, 2))
    return bmi


def get_bmi_state(bmi):
    if bmi < 18:
        return 'underweight'
    elif bmi <= 25:
        return 'standard'
    elif bmi <= 30:
        return 'overweight'
    else:
        return 'obesity'



def main():
    result_bmi = calculate_bmi(*get_user_params())
    status = get_bmi_state(result_bmi)
    print(status)

# try:
#     get_user_params()
# except ValueError:
#     print("błędna wartość")
# except ZeroDivisionError:
#     print("błędna wartość")






if __name__ =="__main__":
    main()

