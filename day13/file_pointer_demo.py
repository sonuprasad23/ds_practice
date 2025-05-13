import os
file_path = "day13/pointer_data.txt"

with open(file_path, "w") as f:
    f.write("ABCDEFGHIJ")
print(f"'{file_path}' created with 'ABCDEFGHIJ'.")

try:
    with open(file_path, "r") as f:
        print(f"\nInitial position: {f.tell()}") # Should be 0

        chunk1 = f.read(3) # Read 'ABC'
        print(f"Read 3 chars: '{chunk1}'")
        print(f"Position after reading 3 chars: {f.tell()}") # Should be 3

        f.seek(5) # Move pointer to index 5 (before 'F')
        print(f"Position after seek(5): {f.tell()}") # Should be 5

        chunk2 = f.read() # Read from 'F' to 'J'
        print(f"Read remaining: '{chunk2}'")
        print(f"Position after reading rest: {f.tell()}") # Should be 10

        f.seek(0, os.SEEK_END) # Go to the end of the file (offset 0 from end)
                               # os.SEEK_SET (0) for beginning, os.SEEK_CUR (1) for current
        print(f"Position after seek(0, os.SEEK_END): {f.tell()}") # Should be 10

        f.seek(-3, os.SEEK_END) # Go 3 bytes back from the end
        print(f"Position after seek(-3, os.SEEK_END): {f.tell()}") # Should be 7
        chunk3 = f.read() # Read 'HIJ'
        print(f"Read from 3 back from end: '{chunk3}'")

except FileNotFoundError:
    print(f"Error: '{file_path}' not found.")