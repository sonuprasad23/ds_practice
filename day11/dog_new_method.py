class Animal:
    def __init__(self, name, sound="generic sound"): self.name, self.sound = name, sound
    def make_sound(self): print(f"{self.name} (Animal) says {self.sound}!")

class Dog(Animal):
    def __init__(self, name): super().__init__(name, sound="Woof")
    def make_sound(self):
        super().make_sound()
        print(f"{self.name} (Dog) also barks loudly!")
    def fetch(self, item): # New method specific to Dog
        print(f"{self.name} fetches the {item}.")

# Test Dog
spot = Dog("Spot")
spot.make_sound()
spot.fetch("ball")