word_counts={}

words=["apple", "banana", "apple", "orange", "banana", "apple"]

for word in words:
    current_count= word_counts.setdefault(word,0)
    word_counts[word]=current_count+1


print(f"Word counts: {word_counts}")

word_counts_get={}
for word in words:
    word_counts_get[word]= word_counts_get.get(word,0)+1

print(f"Word counts using get : {word_counts_get}")