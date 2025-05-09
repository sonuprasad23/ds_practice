import math
class Shape:
    def __init__(self, color): self.color = color
    def area(self): raise NotImplementedError("Subclass must implement")
    def display_color(self): print(f"Color: {self.color}")
class Circle(Shape):
    def __init__(self, color, radius): super().__init__(color); self.radius=radius
    def area(self): return math.pi * self.radius**2
class Square(Shape):
    def __init__(self, color, side): super().__init__(color); self.side=side
    def area(self): return self.side**2

shapes = [
    Circle("Yellow", 3),
    Square("Green", 2),
    Circle("Purple", 1),
    Square("Orange", 5)
]

print("Demonstrating Polymorphism:")
for shape_obj in shapes:
    print(f"\nProcessing a {type(shape_obj).__name__}:")
    shape_obj.display_color()
    print(f"  Area: {shape_obj.area():.2f}")