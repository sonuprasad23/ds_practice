try:
    num1_str = input("Enter numerator: ")
    num2_str = input("Enter denominator: ")

    num1 = float(num1_str)
    num2 = float(num2_str)

    result = num1/num2
    print(f"Result of {num1}/{num2} is {result}")

except ZeroDivisionError:
    print("Error cannot divide by zero")
except ValueError:
    print(f"Error invalid input: PLease enter numeric values")

except Exception as e:
    print(f"An unexpected error occured: {e}")