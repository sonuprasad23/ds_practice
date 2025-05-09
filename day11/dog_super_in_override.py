class Animal:
    def __init__(self, name, sound="generic sound"):
        self.name = name
        self.sound = sound
        print(f"Animal '{name}' init with sound '{sound}'")
    def make_sound(self):
        print(f"{self.name} (Animal) says {self.sound}!")

class Dog(Animal):
    def __init__(self, name):
      
        super().__init__(name, sound="Woof")
        print(f"Dog '{name}' init complete.")

    def make_sound(self):
        super().make_sound()
        print(f"{self.name} (Dog) also barks loudly!")


fido = Dog("Fido")
fido.make_sound()