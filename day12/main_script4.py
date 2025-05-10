import geometry.circle
import geometry.rectangle

c_area = geometry.circle.area(5)
c_circ = geometry.circle.circumference(5)

r_area = geometry.rectangle.area(4, 6)
r_perm = geometry.rectangle.perimeter(4, 6)

print(f"Circle (radius 5) Area: {c_area:.2f}, Circumference: {c_circ:.2f}")
print(f"Rectangle (4x6) Area: {r_area}, Perimeter: {r_perm}")