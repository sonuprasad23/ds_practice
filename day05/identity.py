# day05/identity.py
list_a = [1, 2]
list_b = [1, 2]
list_c = list_a

# == checks if the *values* are the same
print(f"list_a == list_b: {list_a == list_b}") # True, values are equal

# is checks if they refer to the *exact same object* in memory
print(f"list_a is list_b: {list_a is list_b}") # False, different objects in memory

# list_c is assigned to list_a, so they refer to the same object
print(f"list_a is list_c: {list_a is list_c}") # True, same object in memory