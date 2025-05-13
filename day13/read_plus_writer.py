# day13/read_plus_writer.py
file_path = "day13/output_r_plus.txt"

# Initial content
with open(file_path, "w") as f:
    f.write("Original Content Line 1\nOriginal Content Line 2\n")
print(f"'{file_path}' initialized.")

try:
    with open(file_path, "r+") as f: # 'r+' for read and write
        print("\n--- Reading initial content ---")
        initial_content = f.read()
        print(initial_content.strip())

        print("\n--- Writing 'New ' at the beginning ---")
        f.seek(0) # Go to the beginning of the file
        f.write("New ") # This will overwrite the first 4 characters
        # Note: If what you write is shorter than what was there,
        # the rest of the old content on that line remains unless overwritten.

        print("\n--- Reading after writing 'New ' ---")
        f.seek(0) # Go back to the beginning to read again
        modified_content_part = f.read(10) # Read first 10 chars
        print(f"First 10 chars: '{modified_content_part}'")

        f.seek(0)
        modified_content_full = f.read()
        print("\n--- Full modified content ---")
        print(modified_content_full.strip())

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except IOError as e:
    print(f"An IO error occurred: {e}")