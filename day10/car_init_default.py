class Car:
    def __init__(self, color, make = "Unknown"):
        """Initializes a Car object with color and make."""
        self.color = color
        self.make = make

car_default_make = Car("Green")
car_specifie_make = Car("Black", "Tesla")

print(f"Car (default make): Color={car_default_make.color}, Make={car_default_make.make}")
print(f"Car (specified make): Color={car_specifie_make.color}, Make={car_specifie_make.make}")