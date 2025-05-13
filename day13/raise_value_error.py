def process_positive_number(num):
    """Processes a number only if it's positive.
    Raises ValueError if num is not positive."""
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be a number (int or float).")
    if num <= 0:
        raise ValueError(f"Number must be positive, but got {num}.")
    print(f"Processing positive number: {num}")
    return num * 2 

try:
    print(process_positive_number(10))
    print(process_positive_number(0)) 
except ValueError as e:
    print(f"Caught ValueError: {e}")
except TypeError as e:
    print(f"Caught TypeError: {e}")

try:
    print(process_positive_number(-5))
except ValueError as e:
    print(f"Caught ValueError: {e}")

try:
    print(process_positive_number("abc"))
except TypeError as e:
    print(f"Caught TypeError: {e}")