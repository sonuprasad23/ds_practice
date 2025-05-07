class Point:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord

    def display_coords(self):
        """Prints the current coordinates."""
        print(f"Point at ({self.x}, {self.y})")
        
    def move(self, dx, dy):
        """Moves the point by dx and dy."""
        self.x += dx
        self.y += dy
        print(f"Point moved to ({self.x}, {self.y})")

p1 = Point(3,5)
p1.display_coords()
p1.move(2, -1)
p1.display_coords()