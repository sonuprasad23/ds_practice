try:
    num1_str = input("Enter numerator")
    num2_str = input("Enter denominator")

    num1 = float(num1_str)
    num2 = float(num2_str)

    result = num1/num2
    print(f"Result of {num1}/{num2} is {result}")

except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    # This block runs ONLY if NO exceptions occurred in the try block
    print(f"Result of {num1} / {num2} = {result}")
    print("Division successful.")

    