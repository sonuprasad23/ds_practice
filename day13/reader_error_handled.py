file_path = "day13/non_existent_file.txt"
print(f"Attempting to open '{file_path}")
try:
    with open(file_path, "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print(f"Error: The file {file_path} was not found. Please check the path.")

except IOError as e:
    print(f"An IO error occured:{e}")
print("Script finished attempt.")

