d2= {"apple":"green", "banana":"yellow", "grape": "purple", "orange":"orange"}

print(f"Starting d2: {d2}")

print("popping items (LIFO order in 3.7+):")


try:
    while True:
        removed_item = d2.popitem()
        print(f"Removed {popitem}")

except KeyError:
    print("Dictionary is not empty.")

print(f"Final d2: {d2}")