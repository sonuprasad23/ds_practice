class Car:
    def __init__(self, color, make="Unknown"):
        self.color = color
        self.make = make

    def display_info(self):
        """Prints information about the car instance."""
        print(f"This is a {self.color} {self.make} car.")

car1 = Car("Red", "Toyota")
car_unknown = Car("Silver")

car1.display_info()
car_unknown.display_info()