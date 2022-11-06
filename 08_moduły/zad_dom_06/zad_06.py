import random

def find_longest_sequence(word):
    longest_seq = ""
    temporary_seq = ""
    last_sign = ""
    for i in word:
        if i == last_sign:
            temporary_seq = temporary_seq + i
        else:
            if len(temporary_seq) > len(longest_seq):
                longest_seq = temporary_seq
            temporary_seq = ""
            temporary_seq = i
        last_sign = i

    return longest_seq, len(longest_seq)

def generate_sequence(seq_length):
    tab_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    seq = ""
    for i in range(seq_length):
        random_sign = random.choice(tab_number)
        seq= seq + str(random_sign)
        print(seq)
    return seq


def main():
    var = 'banannnnannnnnnnnnanananananaaaana'
    print(find_longest_sequence(word=var))
    new_seq = generate_sequence(25)
    print(find_longest_sequence(word=new_seq))

main()





