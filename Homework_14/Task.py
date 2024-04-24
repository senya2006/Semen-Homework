from predator import Predator

lion = Predator("Vasya", "Lion", "Golden", "lambs")

print(f"{lion.name} is a {lion.species} with {lion.hair_color} hair")

lion.make_sound()
lion.give_birth()
lion.hunt_prey()
