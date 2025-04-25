original=[1,2,[3,4]]

print(f"Original list: {original}, id: {id(original)}")

shallow_copy=original.copy()

print(f"Shallow copy : {shallow_copy}, id: {id(shallow_copy)}")

print(f"Nested list id (original): {id(original[2])}")
print(f"Nested list id (copy) : {id(shallow_copy[2])}")


shallow_copy[0] = 99
print("--- After modifying shallow_copy[0] = 99 ---")
print(f"Original list: {original}")      # Unchanged top-level
print(f"Shallow copy : {shallow_copy}")   # Changed top-level

# Modify element INSIDE the nested list via the copy
shallow_copy[2][0] = 77
print("--- After modifying shallow_copy[2][0] = 77 ---")
print(f"Original list: {original}")      # NESTED list IS changed!
print(f"Shallow copy : {shallow_copy}") 