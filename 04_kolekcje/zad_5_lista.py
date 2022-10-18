ludzie=[
    ["Dorota", "Wellman", "dziennikarka"],
    ["Adam", "Małysz", "sportowiec"],
    ["Robert", "Lewandowski", "piłkarz"],
    ["Krystyna", "Janda", "aktorka"]
]


# for col in row:
#     print(row)

 # for row in ludzie:
    #print(", ".join(row))

for row in ludzie:
    for col in row:
        if col==row[-1]:
            print("-", col)
        else:
            print(col, end=" ")
    