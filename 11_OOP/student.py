class Student:
    university = "UAM"

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


    def email(self):
        return f"{self.firstname}.{self.lastname}@{self.university}.com".lower()

student_A = Student("anna", "Nowak", 23)
student_B = Student("Bartek", "Kowal", 24)


# print("Mam na imie: ",student_A.firstname+" "+student_A.lastname)
# print(student_B.email())
# print(student_A.email())
#
#
student_A.lastname = "Smith"

# print(student_A.__dict__)
# print(Student.__dict__)

quote = "zdrowie jest najwazniejsze"
print(quote.lower())
print(str.upper(quote))
print(Student.email(student_A))