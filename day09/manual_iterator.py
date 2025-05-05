my_list = ['a', 'b']
print(f"List: {my_list}")

my_iter = iter(my_list)
print(f"Iterator object: {my_iter}")

print("\nCalling next() manually:")
item1 = next(my_iter)
print(f"First item: {item1}")

item2 = next(my_iter)
print(f"Second item: {item2}")

try:
    item3 = next(my_iter)
    print(f"Third item: {item3}")

except StopIteration:
    print("\nStopIteration caught on third call, as expected")
    