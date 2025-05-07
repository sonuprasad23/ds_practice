class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def display_dims(self):
        """Prints the dimensions of the rectangle"""
        print(f"Rectangle: Width = {self.width}, Height = {self.height}")

rect1 = Rectangle(10, 20)
rect1.display_dims()
area1 = rect1.calculate_area()
print(f"Area of rect1: {area1}")

