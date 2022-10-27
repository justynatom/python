import random

def get_category():
    message = """ Witaj w grze wisielec

    wybierz kategorie:
    
    1-'wierzeta'
    2-'warzywa' """


def get_words(category):
    filename = file_to_open[category]
    with open(filename) as fopen:
        content = fopen.read()

    return content.split(", ")


file_to_open = {
    "1": "zwierzeta.txt",
    "2": "warzywa.txt"
 }

def show_word_state(letters):
    print(''.join(letters))

def get_letter():
    while True:
        letter = input("Podaj litere: ")
        if len(letter) >1:
            print("To nie jest pojedyncza litera!")
        elif not letter.isalpha():
            print("Ten znak nie jest literą")
        else:
            print(f"Podano litere {letter}")

        return letter

def main():
    category =  get_category()
    words = get_words(category)
    word_to_guess = list(random.choice(words))


    print(word_to_guess)

    user_word = ['-'] *len(word_to_guess)

    show_word_state(user_word)


    tries = 5

    while tries > 0:
        letter = input("Podaj litere do zgadnięcia: ")

        if letter in word_to_guess:
            print(f'Litera {letter} występuje')
            for index, value in enumerate(word_to_guess):
                if letter == value:
                    user_word[index] = letter
            show_word_state()
        else:
            print(f'litera {letter} nie występuje w słowie')
            tries -=1


main()