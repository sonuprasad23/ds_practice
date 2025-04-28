s1= {1,2}
s2= {1,2,3,4}

s3= {1,3}

print(f"s1: {s1}, s2: {s2}, s3: {s3}")
print(f"s1<=s2? {s1<=s2}")
print(f"s1.issubset(s2)?: {s1.issubset(s2)}")

print(f"s2>= s1? {s2>=s1}")
print(f"s2.issuperset(s1)?: {s2.issuperset(s1)}")

print(f"s1 <= s3? {s1 <= s3}")
print(f"s1 <= s2? {s1 <= s2}")