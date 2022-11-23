class Student:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age


    def __str__(self):
        return f'Student: {self.name.capitalize()}{self.lastname.capitalize()}- age:{self.age}'

    @property
    def email(self):
        return self.name + '.' + self.lastname+"@university.com"

    @property
    def fullname(self):
        return f'{self.name}{self.lastname}'

    @fullname.setter
    def fullname(self, first_last):
        self.name, self.last = first_last.split()


    @fullname.deleter
    def fullname(self):
        self.name = None
        self.last =None
        print("dane usuniete")

student_anna= Student('ana', 'kowalska', 23)
print(student_anna)
print(student_anna.email)

student_anna.name = "anna"
print(student_anna)
print(student_anna.email)

student_anna.fullname = 'iga nowak'

del student_anna.fullname
print(student_anna.name, student_anna.last, student_anna.age)
