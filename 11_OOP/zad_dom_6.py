class Employee:
    def __init__(self, position, salary, name, last_name, seniority, student):
        self.position = position
        self.salary = salary
        self.name = name
        self.last_name = last_name
        self.seniority = seniority
        self.company_name = "lovepythoncompany"
        self.student = student

       #list=["b","c","d","f","g","h","j","k","l","m","n","p","r","s","t","x","w","z"]

    def email(self):
        list=""
        list_consonent = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "x", "w", "z"]
        full_name = self.name + self.last_name
        for letter in full_name.lower():
            if letter in list_consonent:
                list += letter
        list += "@"+self.company_name+".com"
        self.email = list
        #print(self.email)
        return list

    def salary_raise(self, percent):
        self.salary = self.salary + percent * self.salary
        print(self.salary)

    def calculate_tax(self):
        tax = self.salary * 0.12
        if self.student == True:
            healty_tax = 0
        else:
            healty_tax = self.salary * 0.03
        return tax+healty_tax






jan_kowalski = Employee("kasjer", 1200, "Jan", "Kowalski", 3, True)
print(jan_kowalski.email())
jan_kowalski.salary_raise(0.1)
print(jan_kowalski.calculate_tax())
