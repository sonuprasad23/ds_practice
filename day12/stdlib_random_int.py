# day12/stdlib_random_int.py
import random

print(f"Random integer (1 to 6): {random.randint(1, 6)}") # Inclusive
print(f"Random integer (0 to 99 from range): {random.randrange(100)}")
print(f"Random integer (10 to 20, step 2): {random.randrange(10, 21, 2)}") # 10,12..20