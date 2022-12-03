def can_be_card_number(number):
    if number.isnumeric() and 13 <= len(number) <= 16:
        return True
    else:
        print("Nie to nie jest numer karty :D")
        return False


def is_visa(number):
    return True if number[0] == '4' and len(number) in [13, 16] else False


def is_mastercard(number):
    return True if len(number) == 16 and \
                   (51 <= int(number[0:2]) <= 55 or 2221 <= int(number[0:4]) <= 2720) else False


def is_american_express(number):
    return True if len(number) == 15 and number[0:2] in ['34', '37'] else False

def read_file(filename):
    f = open(filename)
    return f.readlines()

def save_to_file(number_card, filename):
    with open(filename, "a") as f:
        f.write('\\n' + number_card)


def main():
    cards = read_file("number_cards.txt")
    for card in cards:
        print(card.strip())
        card = card.strip()
        if can_be_card_number(card):
            if is_visa(card):
                print("To jest karta Visa")
                save_to_file(card,"visa.txt")
            elif is_mastercard(card):
                print("To jest MasterCard")
                save_to_file(card,"mastercard.txt")
            elif is_american_express(card):
                print("To jest AmericanExpress")
                save_to_file(card,"americanexpress.txt")
            else:
                print("Nie znany numer karty")

main()