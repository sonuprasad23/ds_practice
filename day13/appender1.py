file_path = "day13/output1.txt" 

with open(file_path, "a") as f: 
    f.write("This is an appended line.\n")
    f.write("Another appended line.\n")
print(f"Data appended to {file_path}")

# with open(file_path, "r") as f_read:
#     print("\nContents of output1.txt after append:")
#     print(f_read.read())