file_path = "day13/output1.txt"
try:
    with open(file_path, "r") as f:
        print(f"--- Content of {file_path} (iterating directly over file object) ---")
        for line in f: 
            print(line.strip())
        print("--- End of Content ---")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")