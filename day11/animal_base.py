class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound=sound
        print(f"Animal {self.name} created")

    def make_sound(self):
        print(f"Animal {self.name} says {self.sound}!")

generic_animal = Animal("Creature", "Hmm")
generic_animal.make_sound()