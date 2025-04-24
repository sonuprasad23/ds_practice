# day05/fstring_format.py
import math # Use math.pi for more precision
pi = math.pi
item = "Laptop"
price = 1200

print(f"Pi formatted to 3 decimals: {pi:.3f}")
# : adds formatting spec
# , adds comma as thousands separator
# .2f formats as float with 2 decimal places
print(f"Item: {item}, Price: $ {price:,.2f}")