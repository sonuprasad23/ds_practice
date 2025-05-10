# day12/stdlib_math_functions.py
import math

num = 16.7
base = 2
exponent = 5
fact_num = 5

print(f"sqrt({num}): {math.sqrt(num):.2f}")
print(f"pow({base}, {exponent}): {math.pow(base, exponent)}") # 2**5
print(f"ceil({num}): {math.ceil(num)}")   # Rounds up
print(f"floor({num}): {math.floor(num)}") # Rounds down
print(f"factorial({fact_num}): {math.factorial(fact_num)}") # 5*4*3*2*1
print(f"log10(1000): {math.log10(1000)}")
print(f"degrees(math.pi/2): {math.degrees(math.pi/2)}") # Convert radians to degrees
print(f"radians(90): {math.radians(90)}") # Convert degrees to radians