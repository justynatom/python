text=input("podaj zdanie: ")
text=text.replace(" ","")
text.lower()
print('jest palidrom-> ', text==text[::-1])


# palindrom=input("Podaj dowolne zdanie,aby sprawdzic czy jest palindromem: ")
# if palindrom==palindrom[::-1]:
#     print("twoje zdanie jest palidromem.")
# else:
#     print("twoje zdanie nie jest palidromem")