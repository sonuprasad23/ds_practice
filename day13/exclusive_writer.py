file_path = "day13/output_x.txt"
try:
    with open(file_path, "x") as f: # 'x' for exclusive creation
        f.write("Created exclusively!\n")
    print(f"File '{file_path}' created and written to.")
except FileExistsError:
    print(f"Error: File '{file_path}' already exists. Cannot create exclusively.")
except IOError as e:
    print(f"An IO error occurred: {e}")