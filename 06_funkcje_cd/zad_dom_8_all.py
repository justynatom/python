def add_car_info_to_dict():
    nowy_wpis_marka_sam = input("Podaj marke samochodu: ")
    samochod["marka"].append(nowy_wpis_marka_sam)
    nowy_wpis_model_sam = input("Podaj model samochodu: ")
    samochod["model"].append((nowy_wpis_model_sam))
    nowy_wpis_rocznik = int(input("Podaj rocznik samochodu: "))
    samochod["rocznik"].append(nowy_wpis_rocznik)

def check_if_car_is_antique():
    if samochod["rocznik"][0] <= 1997:
        print("Gratulacje! Twój samochód " + samochod["marka"][0] + " może być zarejestrowany jako zabytek")
    else:
        print("Twój samochód", samochod["marka"][0], "jest jeszcze zbyt młody")

def modify_values_in_dict():
    # zmodyfikuj wartości w slowniku:
    samochod["marka"][0] = "opel"
    samochod["model"][0] = "astra"
    samochod["rocznik"][0] = 1990


samochod= {
    "marka": [],
    "model": [],
    "rocznik": []
}

print(samochod)

add_car_info_to_dict()
check_if_car_is_antique()

print(samochod)

modify_values_in_dict()

print(samochod)
check_if_car_is_antique()

print(samochod)

