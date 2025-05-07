class Car:
    def __init__(self, color, make):
        """Initializes a Car object with color and make."""
        print(f"Initializing a {color} {make} car...")
        self.color = color
        self.make = make

car1 = Car("Red", "Toyota")
car2 = Car("Blue", "Honda")


print(f"Car1 : Color: {car1.color}, Make: {car1.make}")
print(f"Car2 : Color: {car2.color}, Make: {car2.make}")
