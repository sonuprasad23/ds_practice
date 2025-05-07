def print_all(p1,p2, *args, **kwargs):
    """Print all types of arguments received:"""
    print(f"\nPositional p1: {p1}")
    print(f"\nPositional p2: {p2}")
    print(f"Extra positional args (*args):{args}")
    print(f"Extra keyword args (**kwargs): {kwargs}")


print_all(1,2)
print_all(1,2,3,4,5)
print_all(1,2,name="A", city="B")
print_all(1,2,3,4,name="A", city= "B")
print_all(1, 2, *(5, 6), **{'name': 'C', 'id': 99}) 


