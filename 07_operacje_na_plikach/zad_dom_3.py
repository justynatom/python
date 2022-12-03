import os

from zad_1 import open_file, show

def main():
    quotes = open_file()
    for index in range(5):
        show(quotes[index])

    # quote = quotes[0]
    # show(quote)



main()


# for quote in range(5):
#     print(quote)
