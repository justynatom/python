def get_words():
    filename = 'tekst.txt'
    with open(filename, 'r', encoding="utf-8") as file:
        content = file.read().split()
    return content

def find_longest_word(words):
    longest = ''

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def main():
    word_list= get_words()
    print(find_longest_word(word_list))



main()