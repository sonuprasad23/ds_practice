def print_args(*args):
    """Print the args tuple and each argument"""
    print(f"\nRecieverd args (type{type(args)}): {args}")
    print("Arguments:")
    for arg in args:
        print(f"-{arg}")


print_args(1,2)
print_args("a", "b", "c", True)
print_args()