txt = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

txt = txt.lower()
txt = txt.replace(',', ' ')
txt= txt.split()
print(txt)

# print("szybko: ", txt.count("szybko"))
# print("zbudź: ", txt.count("zbudź"))

# uniq_word=set(txt)
# print(uniq_word)
#
# for word in uniq_word:
#     print(f"{word}-> {txt.count(word)}")


counting_dict={}

for w in txt:
    if w not in counting_dict:
        counting_dict[w]=1
    else:
        counting_dict[w]+=1

for k, v in counting_dict.items():
    print(k, ":", v)
