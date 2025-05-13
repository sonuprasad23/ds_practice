file_path = "day13/output1.txt"

try:
    with open(file_path, "r") as f: 
        content = f.read()
        print(f"--- Content of {file_path} (using read()) ---")
        print(content)
        print("--- End of Content ---")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found. Run writer1.py first.")