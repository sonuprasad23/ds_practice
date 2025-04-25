unsorted2=[4,0,7,1]
print(f"Original unsorted2: {unsorted2}")

sorted_asc=sorted(unsorted2)

print(f"New sorted ascending list :{sorted_asc}")

sorted_desc=sorted(unsorted2, reverse=True)
print(f"New sorted descending list: {sorted_desc}")

print(f"Original unsorted2 (unchanged): {unsorted2}")