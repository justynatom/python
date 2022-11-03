print("jestem w example_module")

NAMES_FR = ["charles", "geal", "pierre"]

def find_longest_word(words):
    longest = ''

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest