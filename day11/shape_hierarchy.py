import math

class Shape:
    def __init__(self, color):
        self.color = color
        print(f"Shape created with color: {self.color}")

    def area(self):
        raise NotImplementedError("Subclasses must implement the area() method.")

    def display_color(self):
        print(f"This shape's color is {self.color}.")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color) 
        self.radius = radius
        print(f"Circle details: radius={self.radius}")

    def area(self): 
        return math.pi * (self.radius ** 2)

class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
        print(f"Square details: side={self.side_length}")

    def area(self): # Override
        return self.side_length ** 2

my_circle = Circle("Red", 5)
my_square = Square("Blue", 4)

my_circle.display_color()
print(f"Area of circle: {my_circle.area():.2f}")

my_square.display_color()
print(f"Area of square: {my_square.area()}")