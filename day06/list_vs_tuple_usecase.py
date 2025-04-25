moving_point_list=[10.0, 20.0]

moving_point_list[0]+=1.5

print(f"Updated list coords: {moving_point_list}")


# use a tuple if the coordinates represent a fixed point that should not change

#immutability ensures data integrity

landmark_tuple=(40.7128, -74.0060)

# landmark_tuple[0]=41.0 #Will cause TypeError

print(f"Fixed tuple coords: {landmark_tuple}")