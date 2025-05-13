# day13/writer2.py
file_path = "day13/output2.txt"
lines_to_write = [
    "Line A from writelines.\n",
    "Line B is next.\n",
    "Line C is the final one for now.\n"
]
with open(file_path, "w") as f:
    f.writelines(lines_to_write)
print(f"List of strings written to {file_path} using writelines()")