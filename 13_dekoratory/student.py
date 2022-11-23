import datetime


class Student:
    university = "UAM"

    def __init__(self, firstname, lastname, age, student_avg):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.student_avg = student_avg


    def email(self):
        return f"{self.firstname}.{self.lastname}@{self.university}.com".lower()


    def grant_scholarship(self):
        if self.student_avg > self.min_avg:
            print("przyznano stypendium")
        else:
            print("odmowa przyznania")

    @classmethod
    def set_min_avg(cls, aveage):
        cls.min_avg = aveage

    @staticmethod
    def is_academic(day):
        if day.weekday() == 5 or day.weekday() == 6: #sob/niedziela
            return False
        else:
            return True

student_A = Student("anna", "Nowak", 23, 4.8)
student_B = Student("Bartek", "Kowal", 24, 4.5)


# print("Mam na imie: ",student_A.firstname+" "+student_A.lastname)
# print(student_B.email())
# print(student_A.email())
#
#
student_A.lastname = "Smith"

# print(student_A.__dict__)
# print(Student.__dict__)

# quote = "zdrowie jest najwazniejsze"
# print(quote.lower())
# print(str.upper(quote))
print(Student.email(student_A))

today=datetime.date.today()
print(today)

print("do we have academic day today?")
print(Student.is_academic(today))