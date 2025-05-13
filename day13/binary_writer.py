file_path = "day13/data.bin"
byte_data = b'\x48\x65\x6c\x6c\x6f' # "Hello" in ASCII bytes

with open(file_path, "wb") as bf: # 'wb' for write binary
    bf.write(byte_data)
print(f"Binary data written to {file_path}")


try:
    with open(file_path, "rb") as bf_read: # 'rb' for read binary
        read_bytes = bf_read.read()
        print(f"\nRead binary data from {file_path}: {read_bytes}")
        print(f"Decoded as UTF-8 (if applicable): {read_bytes.decode('utf-8', errors='replace')}")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found. Run binary_writer.py first.")