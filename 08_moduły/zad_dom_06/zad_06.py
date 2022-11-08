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

# def is_sequence_valid_old(longest_seq):
#     if len(longest_seq) >= 2:
#         print(longest_seq)
#     else:
#         new_gen_seq = generate_sequence(25)
#         tmp, len_tmp = find_longest_sequence(new_gen_seq)
#     return new_gen_seq, tmp, len_tmp

def is_sequence_valid(generated_seq):
    tmp, len_tmp = find_longest_sequence(generated_seq)
    while len_tmp < 2:
        len_generated_seq = len(generated_seq)
        print("wrong seq: ", generated_seq)
        new_gen_seq = generate_sequence(len_generated_seq)
        generated_seq = new_gen_seq
        tmp, len_tmp = find_longest_sequence(generated_seq)
    return generated_seq

def main():
    var = 'banannnnannnnnnnnnanananananaaaana'
    print(find_longest_sequence(word=var))
    seq_len_user = 10
    new_seq = generate_sequence(seq_len_user)
    new_seq_validated = is_sequence_valid(generated_seq=new_seq)
    print("good seq: ", new_seq_validated)
    print(find_longest_sequence(word=new_seq_validated))

main()





