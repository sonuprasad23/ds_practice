def outer_function(value):
    try:
        print("Outer function trying to divide...")
        result = 100 / int(value)
        print(f"Division result: {result}")
    except ValueError as e:
        print(f"ValueError in outer_function: Invalid input '{value}'. Logging and re-raising.")

        raise ValueError(f"Original input '{value}' was invalid for division.") from e # Python 3: chain exceptions
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError in outer_function. Logging and re-raising.")
        # raise # Re-raises the original ZeroDivisionError
        raise ZeroDivisionError("Attempted to divide by zero in sensitive calculation.") from e
    return "Outer function completed (if no re-raise)"

try:
    print(outer_function(5))
    # print(outer_function(0))
    print(outer_function("abc"))
except (ValueError, ZeroDivisionError) as e_main: # Catch re-raised exceptions
    print(f"\nMain block caught re-raised exception: {type(e_main).__name__} - {e_main}")
    if e_main.__cause__:
        print(f"  Original cause: {type(e_main.__cause__).__name__} - {e_main.__cause__}")