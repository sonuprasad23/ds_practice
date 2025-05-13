file_path = "day13/output1.txt"

with open(file_path, "w") as f:
    f.write("This is the first line.\n")
    f.write("Python file writing is fun.\n")
    f.write("End of file.\n")
    f.write("This is the last line.\n")
print(f"Data written to {file_path}")


#  To verify, you can open output1.txt in your editor or:
# with open(file_path, "r") as f_read:
#     print("\nContents of output1.txt:")
#     print(f_read.read())