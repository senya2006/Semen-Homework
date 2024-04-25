from mammal import Mammal

class Predator(Mammal):
    def __init__(self, name, species, hair_color, prey_type):
        super().__init__(name, species, hair_color)
        self.prey_type = prey_type

    def hunt_prey(self):
        print(f"{self.name} is hunting {self.prey_type}")
        