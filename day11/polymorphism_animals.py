class Animal:
    def __init__(self, name, sound="generic sound"): self.name, self.sound = name, sound
    def make_sound(self): print(f"{self.name} says {self.sound}!")
class Dog(Animal):
    def __init__(self, name): super().__init__(name, sound="Woof")
    def make_sound(self): print(f"{self.name} BARKS: Woof Woof!") 
class Cat(Animal):
    def __init__(self, name): super().__init__(name, sound="Meow")

pets = [
    Dog("Buddy"),
    Cat("Whiskers"),
    Animal("Tweety", "Chirp") 
]

print("Animal Sounds (Polymorphism):")
for pet_obj in pets:
    pet_obj.make_sound() 