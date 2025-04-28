d2 = {"apple": "red", "banana": "yellow", "grape": "purple"}

print(f"Colors of banana: {d2['banana']}")

try:
    print(f"Colors of orange: {d2['orange']}")
except KeyError as e:
    print(f"Error: Key 'orange' not found using []")



orange_color_get = d2.get("orange")
print(f"Color of orange (using get()): {orange_color_get}")

grape_color_get=d2.get("grape", "unknown color")
print(f"Color of grape (using get() w/ default): {grape_color_get}")

apple_color_get= d2.get("apple", "unknown color")
print(f" Color of apple(using get() w/ default): {apple_color_get}")