d2= {"apple":"green", "banana":"yellow", "grape": "purple", "orange":"orange"}

print(f"Original d2: {d2}")

removed_value = d2.pop("grape")

print(f"Removed value for 'grape': {removed_value}")

print(f"d2 after pop ('grape'): {d2}")

try:
    d2.pop("kiwi")

except KeyError:
    print("\nError : Key 'Kiwi' is not found durinh pop()")


kiwi_value = d2.pop("kiwi", "Not found")

print(f"\nResult of pop ('kiwi', 'Not Found): {kiwi_value}")
print(f"d2 remains unchanged: {d2}")

