items=["apple","banana", "cherry","banana"]

print(f"Original items:{items}")

items.remove("banana")

print(f"Items after removing banana: {items}")

try:
    items.remove("grape")
except ValueError :
    print("Grape not found in the list.")