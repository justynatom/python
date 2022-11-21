class Employee:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def show_salary(self):
        print("I have a salary! :)")


class Accountant(Employee):
    def check_billing(self):
        print("The billing is...")


bookkeeper = Accountant('John', 'Snow')
bookkeeper.show_salary()
bookkeeper.check_billing()
        
