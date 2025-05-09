class Animal:
    def __init__(self, name, sound="generic sound"):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}!")


class Cat(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__(name, sound="Meow")

        print(f"Cat {self.name} specifically created")

whiskers = Cat("Whiskers")
whiskers.make_sound()