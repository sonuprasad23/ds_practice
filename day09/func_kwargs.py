def print_kwargs(**kwargs):
    """Prints the kwargs dict and each key-value pair"""
    print(f"\nReceived kwargs (type{type(kwargs)}): {kwargs}")
    print("Keyword Arguments: ")
    for key, value in kwargs.items():
        print(f"-{key}: {value}")


print_kwargs(name= "X", age = 10, city = "Online")
print_kwargs(a=1, b=2, c=True, d=None)
print_kwargs()