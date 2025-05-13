file_path = "day13/output1.txt"
try:
    with open(file_path, "r") as f:
        lines_list = f.readlines() 
        print(f"--- List of lines from {file_path} (using readlines()) ---")
        print(lines_list)

        print("\n--- Printing each line (stripped) from the list ---")
        for line in lines_list:
            print(line.strip()) 
        print("--- End of Content ---")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")