class Dog:
    def __init__(self, name, color_hair, race, age):
        self.name = name
        self.color_hair = color_hair
        self.race = race
        self.age = age


    def bark(self):
        return "Wolf!" * self.age

    def tail_wag(self, number):
        return f"{'machu' * self.age}".center(number, '-')

pixie = Dog("Burek","czarny","mieszaniec", 4)
print(pixie.name)
print(pixie.bark())
print(pixie.tail_wag(4))

dixie= Dog("Dixie", "yellow", "golden", 6)