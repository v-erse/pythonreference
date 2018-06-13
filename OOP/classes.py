class Animal:
    def __init__(self, habitat, diettype):
        self.habitat = habitat
        self.diettype = diettype

    def printHabitat(self):
        print(self.habitat)


lion = Animal("jungle", "carnivore")
print("Habitat: {}\nDiet: {}".format(lion.habitat, lion.diettype))


# Inheritance
class Fish(Animal):
    def __init__(self, colour, diettype, habitat="sea"):
        super().__init__(habitat, diettype)
        self.colour = colour


clownfish = Fish("orange", "omnivore")

# use isinstance to check class types
print(isinstance(clownfish, Fish))
# and issubclass to check for subclass
print(issubclass(Fish, Animal))


class Character():
    def __init__(self, name):
        self.name = name

    def printName(self):
        print(self.name)


# Multiple Inheritance
class NemoCharacter(Fish, Character):
    def __init__(self, colour, diettype, name):
        self.colour = colour
        self.diettype = diettype
        self.name = name
        self.habitat = "sea"


marlin = NemoCharacter("orange", "omnivore", "Marlin")
marlin.printHabitat()  # <- this method comes from Animal, which is extended
# by Fish
marlin.printName()  # <- this method comes from Character
