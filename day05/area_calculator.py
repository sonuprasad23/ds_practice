try:
    length_str=input("Enter the length of the rectangle")
    length=float(length_str)


    width_str=input("Enter the width of the rectangle:")
    width =float(width_str)


    area=length * width

    print(f"The area of the rectangle is : {area}")


except ValueError:
    print("Invalid input. Please enter numeric values for length and width")

    