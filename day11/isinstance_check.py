# day11/isinstance_check.py
# (Assuming Vehicle, Car, Motorcycle classes from previous exercise)
# ... (paste class definitions here or import them) ...
# Re-define for standalone script
class Vehicle:
    def __init__(self, make, model, year): self.make,self.model,self.year = make,model,year
    def display_info(self): print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make,model,year)
        self.num_doors=num_doors
    def display_info(self): super().display_info(); print(f"Doors: {self.num_doors}")
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make,model,year)
        self.type_of_bike=type_of_bike
    def display_info(self): super().display_info(); print(f"Type: {self.type_of_bike}")

my_car = Car("Toyota", "Camry", 2022, 4)
my_bike = Motorcycle("Harley-Davidson", "Sportster", 2021, "Cruiser")

print(f"Is my_car an instance of Car? {isinstance(my_car, Car)}")             
print(f"Is my_car an instance of Vehicle? {isinstance(my_car, Vehicle)}")
print(f"Is my_car an instance of Motorcycle? {isinstance(my_car, Motorcycle)}") 

print(f"\nIs my_bike an instance of Motorcycle? {isinstance(my_bike, Motorcycle)}") 
print(f"Is my_bike an instance of Vehicle? {isinstance(my_bike, Vehicle)}")       
print(f"Is my_bike an instance of Car? {isinstance(my_bike, Car)}")        