set1 = set()
print(f"Initial set1: {set1}")
set1.add(5)

print(f"After adding 5: {set1}")
set1.add(6)

print(f"After adding 6: {set1}")

set1.add(5)
print(f"After adding 5 again: {set1}")

set1.update([6,7,8])
print(f"After updating [6,7,8]: {set1}")