__author__ = 'wombat'
import Animals.Mammal
import Animals.Carnivore

class Dog (Animals.Mammal,Animals.Carnivore):
    # TODO define color
    colors = "brown"
    print(colors)
    print(Animals.Mammal.Mammalia.extremities)
    def sound(self):
        print("bow-wow")

 