# def sprawdzenie_czy_to_jest_karta():
#     czy_to_jest_karta = input("Podaj numer karty: ")
#     if int(czy_to_jest_karta) >= 13 and int(czy_to_jest_karta) <= 16:
#         print("Tak, jest to karta")
#     else:
#         print("Podałeś błednę dane -> to nie jest karta")
#
#
# def jaka_to_firma():
#     poczatkowa_liczba_nr_karty = int(input("Podaj początkowe liczby numeru swojej karty: "))
#     if poczatkowa_liczba_nr_karty == 4:
#         print("Twoja karta to Visa")
#     elif poczatkowa_liczba_nr_karty <= 55 or poczatkowa_liczba_nr_karty >= 51:
#         print("Twoja karta to MasterCard")
#     elif poczatkowa_liczba_nr_karty == 34 or poczatkowa_liczba_nr_karty == 37:
#         print("Twoja karta do American Express")
#
# #numer_karty_uzyt=int(input("Podaj numer swojej karty: "))
# #poczatkowa_liczba_nr_karty=int(input("Podaj początkowe liczby numeru swojej karty: "))
# #czy_to_jest_karta=input("Podaj numer karty: ")
#
#
# #
# # if poczatkowa_liczba_nr_karty == 4:
# #     print("Twoja karta to Visa")
# # elif poczatkowa_liczba_nr_karty <= 55 or poczatkowa_liczba_nr_karty >= 51:
# #     print("Twoja karta to MasterCard")
# # elif poczatkowa_liczba_nr_karty == 34 or poczatkowa_liczba_nr_karty == 37:
# #     print("Twoja karta do American Express")
# #
# # if czy_to_jest_karta >= 13 and czy_to_jest_karta <= 16:
# #     print("Tak, jest to karta")
# # else:
# #     print("Podałeś błednę dane -> to nie jest karta")
#
# #sprawdzenie_czy_to_jest_karta()
# jaka_to_firma()
def can_be_card_number(number):
    if card.isnumeric() and 13 <= len(card) <= 16:
        print("to moze byc nr karty")
        return True
    else:
        print("Nie, to nie jest karta")
        return False


def is_visa(number):
    return True if number[0] =='4' and len(numer) in [13, 16] else False
    # if card[0] == '4' and len(card) in [13, 16]:
    #     return True
    # else:
    #     return False
 def is_mastercard(number):
     return True if len(card) == 16 and (51 <= int(card[0:2]) >=55 or 2221 <= int(card[0:4]) >=2720) else False

card = input("Podaj nr karty: ")

if can_be_card_number(card):
    if card[0] == '4' and len(card) in[13,16]:
        print("To jest Visa.")
    elif len(card) == 16 and (51 <= int(card[0:2]) >=55 or 2221 <= int(card[0:4]) >=2720):
        print("To jest MasterCard.")
    elif len(card) == 15 and card[0:2] in['34', '37'] :
        print("to jest American express")
    else:
        print("Nieznany numer karty")
