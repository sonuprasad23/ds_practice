file_path = "day13/non_existent_file.txt"
print(f"Attempting to open '{file_path}'...")
with open(file_path, "r") as f:
    content = f.read()
    print(content)