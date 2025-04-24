# day05/even_odd.py
try:
    num_str = input("Enter an integer: ")
    num = int(num_str)

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Invalid input. Please enter an integer.")