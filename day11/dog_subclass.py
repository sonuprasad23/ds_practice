class Animal:
    def __init__(self, name, sound="generic sound"):
        self.name = name
        self.sound = sound
        print(f"Animal {self.name} created")

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, sound="Woof")
        print(f"Dog {self.name} specifically created.")


buddy = Dog("Buddy")
buddy.make_sound()
