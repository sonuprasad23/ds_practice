class Dog:
    species = "Cannis Familaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog3 = Dog("Rex", 1)
print(f"Dog3 initial species(from class): {dog3.species}")
print(f"Dog3 class species: {Dog.species}")

Dog.species = "Canis Lupus Familiaris"

print(f"\n-- After changing Dog.species --")
print(f"Dog3 species (reflects small change): {dog3.species}")
print(f"Dog class species: {Dog.species}")

dog3.species = "Domestic wolf"
print(f"\n-- After changing dog3.species --")
print(f"Dog3 species (instance attribute shadows class): {dog3.species}")

print(f"Dog class species:(changed by instance assignment): {Dog.species}")

dog4 = Dog("Spot", 2)
print(f"Dog4 species: {dog4.species}")

