from animal import Animal

class Mammal(Animal):
    def __init__(self, name, species, hair_color):
        super().__init__(name, species)
        self.hair_color = hair_color

    def give_birth(self):
        pass    # also some function only for mammals
    