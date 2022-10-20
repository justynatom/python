example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

tablica=[]
for i in example_list:
    print("i: ", i, "example_list.count(i): ", example_list.count(i))
    if example_list.count(i) <= 1:
        tablica.append(i)
    else:
        example_list.remove(i)
    print(tablica)