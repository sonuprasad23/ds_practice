# day05/number_sign.py
try:
    num_str = input("Enter an integer: ")
    num = int(num_str)

    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
except ValueError:
    print("Invalid input. Please enter an integer.")