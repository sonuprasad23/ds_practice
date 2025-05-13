file_path = "day13/temp_finally.txt"
f = None 
try:
    f = open(file_path, "w") 
    print(f"File '{file_path}' opened.")
    f.write("Testing finally block.\n")
    # Simulate an error:
    # result = 10 / 0
    print("Data written.")
except ZeroDivisionError:
    print("Caught a ZeroDivisionError in try block.")
except IOError as e:
    print(f"IOError in try block: {e}")
finally:
    print("\n--- Finally block executing ---")
    if f: # Check if file object 'f' was successfully created
        print(f"Closing file '{file_path}'.")
        f.close() # Crucial cleanup, especially if not using 'with'
    else:
        print("File object was not created, nothing to close.")
print("Script execution finished.")

# Proper way with 'with' - no explicit close needed in finally
print("\n--- Demonstrating with 'with' statement (recommended) ---")
try:
    with open(file_path, "a") as f_with:
        print(f"File '{file_path}' opened with 'with'.")
        f_with.write("Testing with 'with' and finally.\n")
        # result_with = 10 / 0 # Simulate error
        print("Data written with 'with'.")
except ZeroDivisionError:
    print("Caught ZeroDivisionError inside 'with' block.")
finally:
    # 'finally' still executes, but f_with is already guaranteed to be closed
    print("Finally block after 'with' statement.")