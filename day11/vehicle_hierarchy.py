class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print(f"Vehicle created: {self.year} {self.make} {self.model}")

    def display_info(self):
        print(f"--- Vehicle Info ---")
        print(f"  Make: {self.make}")
        print(f"  Model: {self.model}")
        print(f"  Year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year) 
        self.num_doors = num_doors
        print(f"Car subclass details added: {self.num_doors} doors")

    def display_info(self): 
        super().display_info() 
        print(f"  Doors: {self.num_doors}") 

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike
        print(f"Motorcycle subclass details added: {self.type_of_bike} type")

    def display_info(self): # Override
        super().display_info()
        print(f"  Type: {self.type_of_bike}")


my_car = Car("Toyota", "Camry", 2022, 4)
my_bike = Motorcycle("Harley-Davidson", "Sportster", 2021, "Cruiser")

print("\nDisplaying Car Info:")
my_car.display_info()
print("\nDisplaying Motorcycle Info:")
my_bike.display_info()