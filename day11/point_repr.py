class Point:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    def __str__(self):
        return f"Point coordinates: ({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x_coord={self.x}, y_coord={self.y})"

p1 = Point(10, 20)
print(f"str(p1): {str(p1)}")
print(f"repr(p1): {repr(p1)}")
print(f"p1 in list: {[p1]}") 