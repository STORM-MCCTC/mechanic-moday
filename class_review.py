# what is a class?
# Blueprint - a preplanned layout to create an object.
# What can an object have? Attributes (Variables),  Methods (Functions), Identity 

#create the class, the blueprint to create future objects
class Dinosaur:
    #make the constructor
    def __init__(self, name, species, diet):
        self.name = name #dinos name
        self.species = species #dinos Species
        self.diet = diet  #dinos deit

    #create method - action the dinos can do
    def rawr(self):
        print(f"{self.name} lets out a mighty RAAAAAAAAWWWWRR")

    def eat(self, food):
        if food == self.diet:
            print(f"{self.name} eats {food}... Mmm... Delish. Uncle Roger agrees")
        else:
            print(f"{self.name} doesn't eat {food}")

    def info(self):
        print(f"{self.name} is a {self.species} and eats {self.diet}")

Trex = Dinosaur("Steve", "Tyrannosarus Rex", "Meat")
Spike = Dinosaur("Spike", "Stegosaurus", "Plants")
George = Dinosaur("George", "Pterodactyl", "Everything")

Trex.rawr()
Trex.eat("Meat")
Trex.info()
print("\n")
Spike.rawr()
Spike.eat("Plants")
Spike.info()
print("\n")
George.rawr()
George.eat("Everything")
George.info()
print("\n")
