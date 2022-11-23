def closer():
    number =4

    def nested_function(text):
        #print("Jestem w środku!!")
        return text * number

    return nested_function


variable = closer() #variable=nested_function
print(variable("Jestem w srodku- "))


