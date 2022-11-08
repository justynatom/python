def open_file(filename):
    while True:
        try:
            with open(filename) as file:
                return file.readlines()
        except FileNotFoundError:
            print("nie ma takiego pliku")
            filename = input("Podaj nawe pliku: ")

namefile = "test.txt"
content = open_file(namefile)
print(content)

