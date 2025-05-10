import sys

print(f"Command-line arguments (sys.argv): {sys.argv}")
print(f"Script name: {sys.argv[0]}")
if len(sys.argv) > 1:
    print("Other arguments:")
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"  Arg {i}: {arg}")
else:
    print("No additional arguments provided.")  