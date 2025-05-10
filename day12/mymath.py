"""A simple math module."""
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y

PI = 3.14159
if __name__=="__main__":
    print("mymath.py is being run directly.")
    print(f"Test add (5,3): {add(5,3)}")
    print(f"Test suubtract(16,3): {subtract(16,3)}")
    print(f"Module PI: {PI}")