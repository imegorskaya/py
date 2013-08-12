from Animals.Carnivore import Carnivore
from Animals.Herbivore import Herbivore

__author__ = 'wombat'
class Mammalia(object):
    extremities = 4
    def feeds(self):
        print ("milk")
    def proliferates(self):
        pass
class Marsupial(Mammalia):
        def proliferates(self):
            print("poach")
class Eutherian(Mammalia):
        def proliferates(self):
            print("placenta")

class TasmanianDevil(Marsupial, Carnivore):
    pass

class Duckbill(Marsupial, Herbivore):
    pass

class Cat(Carnivore, Eutherian):
    # TODO define color
    colors = "stripes and points"
    print(colors)
    print(Mammalia.extremities)
    def sound(self):
        print("miaou")

class Tiger(Eutherian,Carnivore):
    pass

class Cow(Eutherian, Herbivore):
# todo define color
    colors = "black and white"
    print(colors)
    print(Mammalia.extremities)
    def sound(self):
        print("mooo")
