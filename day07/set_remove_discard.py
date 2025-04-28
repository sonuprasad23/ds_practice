set1 = {5,6,7,8}
print(f"Original set1: {set1}")

set1.remove(7)
print(f"After removing 7: {set1}")

set1.discard(6)
print(f"After discarding 6 : {set1}")

set1.discard(10)
print(f"After discarding 10(not present): {set1}")

try:
    set1.remove(10)

except KeyError:
    print("Error: Element 10 not found using rmeove().")