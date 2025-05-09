class Animal:
    def __init__(self, name, sound="generic sound"):
        self.name = name
        self.sound = sound
    def make_sound(self): print(f"{self.name} says {self.sound}!")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, sound="Woof Woof") 

    def make_sound(self):
         print(f"{self.name} says {self.sound}")

rover = Dog("Rover")
rover.make_sound()