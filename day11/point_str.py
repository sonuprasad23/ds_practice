class Point:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    def __str__(self): 
        return f"({self.x}, {self.y})"

p1 = Point(7, 2)
print(p1) 
print(str(p1)) 