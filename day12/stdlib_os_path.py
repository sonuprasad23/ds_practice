import os

file_path_parts = ['data', 'raw', 'file.csv']
constructed_path = os.path.join(*file_path_parts) 
print(f"Constructed path: {constructed_path}")

mymath_file = "mymath.py" 
if os.path.exists(mymath_file):
    print(f"'{mymath_file}' exists.")
    print(f"  Absolute path: {os.path.abspath(mymath_file)}")
    print(f"  Is it a file? {os.path.isfile(mymath_file)}")
    print(f"  Is it a directory? {os.path.isdir(mymath_file)}")
else:
    print(f"'{mymath_file}' does NOT exist where expected.")

geometry_dir = "geometry"
if os.path.exists(geometry_dir):
    print(f"'{geometry_dir}' exists.")
    print(f"  Is it a file? {os.path.isfile(geometry_dir)}")
    print(f"  Is it a directory? {os.path.isdir(geometry_dir)}")