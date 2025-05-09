import functools

@functools.total_ordering # Decorator to fill in missing comparison methods
class Dimension:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height

    def __eq__(self, other):
        """Checks if two Dimension objects are equal based on area."""
        if not isinstance(other, Dimension):
            return NotImplemented # Important for inter-type comparisons
        print(f"Comparing {self} == {other}")
        return self.area == other.area

    def __lt__(self, other):
        """Checks if this Dimension is less than another based on area."""
        if not isinstance(other, Dimension):
            return NotImplemented
        print(f"Comparing {self} < {other}")
        return self.area < other.area

    def __repr__(self):
        return f"Dimension(w={self.width}, h={self.height}, area={self.area})"

d1 = Dimension(2, 3) # area 6
d2 = Dimension(3, 2) # area 6
d3 = Dimension(1, 5) # area 5
d4 = Dimension(4, 2) # area 8

print(f"d1 == d2: {d1 == d2}") # True
print(f"d1 != d3: {d1 != d3}") # True (derived by total_ordering)
print(f"d3 < d1: {d3 < d1}")   # True
print(f"d1 > d3: {d1 > d3}")   # True (derived)
print(f"d4 >= d1: {d4 >= d1}") # True (derived)
print(f"d1 <= d4: {d1 <= d4}") # True (derived)
# print(d1 == 5) # Will use NotImplemented and likely be False