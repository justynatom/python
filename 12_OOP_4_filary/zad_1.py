class Animal:
    heterotroph = "TAK"

    def __init__(self):
        print("Zwierzeta")


class Mammal(Animal):
    def __init__(self):
        print("Ssaki")

    def feed_baby(self):
        print('Pije mleko matki')


class Cat(Mammal):
    def __init__(self):
        print("Kot")

    def feed_baby(self):
        super().feed_baby()
        print("Kotka zapewnia kociętom opiekę przez mniej więcej 3 miesiące")


class Dog(Mammal):
    def __init__(self):
        print("Pies")


class Human(Mammal):
    def __init__(self):
        print("Człowiek")

animal = Animal()
print("Czy cudzożywny:", animal.heterotroph)
print('---------')
mammal = Mammal()
print("Czy cudzożywny:", mammal.heterotroph)
mammal.feed_baby()
print('---------')
cat = Cat()
print("Czy cudzożywny:", cat.heterotroph)
cat.feed_baby()