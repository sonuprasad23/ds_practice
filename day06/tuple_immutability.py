my_tuple=(1,2,3)

print(f"Original tuple : {my_tuple}")

try:
    my_tuple[0]=99

except TypeError as e:
    print(f"\n Error trying to modify tuple: {e}")
    print("Tuples are immutable!")

    