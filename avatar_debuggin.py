import pdb
pdb.set_trace()

class Character:
    def __init__(self, name, element):
        self.name = name
        self.element = element
        pdb.set_trace()

    def introduce(self):
        return f"My name is {self.name}, and I am a {self.element} bender."

aang = Character("Aang", "Air")
pdb.set_trace()
katara = Character("Katara", "Water")
pdb.set_trace()
toph = Character("Toph", "Earth")
pdb.set_trace()

def journey_to_element(character):
    if character.element == "Air":
        pdb.set_trace()
        return "Aang flies with his glider."
    elif character.element == "Water":
        pdb.set_trace()
        return "Katara bends water to travel."
    elif character.element == "Earth":
        pdb.set_trace()
        return "Toph creates earth walls to move forward."
    else:
        pdb.set_trace()
        return "This character does not have an elemental power!"

pdb.set_trace()
print(aang.introduce())
print(journey_to_element(aang))
pdb.set_trace()
print(katara.introduce())
print(journey_to_element(katara))
pdb.set_trace()
print(toph.introduce())
print(journey_to_element(toph))
pdb.set_trace()