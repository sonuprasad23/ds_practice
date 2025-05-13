file_path = "day13/output1.txt"

try:
    with open(file_path, "r") as f:
        print(f"--- Content of {file_path} (using readline() in loop) ---")
        while True:
            line = f.readline() 
            if not line: 
                break
            print(line, end='') 
        print("--- End of Content ---")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")