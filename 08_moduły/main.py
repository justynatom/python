#import example_module as em
from example_module import find_longest_word , NAMES_FR
from random import randint


names = ['Laura', 'Anna', 'Vicky', 'Patrick', 'kunegundaaa']

max_len_name = find_longest_word(names)

print(max_len_name)
print(NAMES_FR)

print(randint(1, 20))