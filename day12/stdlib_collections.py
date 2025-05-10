from collections import Counter, defaultdict, deque

# --- Counter ---
my_list_for_counter = ['a', 'b', 'c', 'a', 'b', 'a', 'd']
counts = Counter(my_list_for_counter)
print(f"Counter: {counts}")
print(f"Count of 'a': {counts['a']}")
print(f"Most common (2): {counts.most_common(2)}")

# --- defaultdict ---
# defaultdict with int (for counting, default is 0)
dd_int = defaultdict(int)
for item in my_list_for_counter:
    dd_int[item] += 1
print(f"defaultdict(int) for counts: {dd_int}")
print(f"Accessing new key 'x' in dd_int: {dd_int['x']}") 
print(f"dd_int after accessing 'x': {dd_int}")

# defaultdict with list (for grouping)
words = ["apple", "ant", "ball", "bat", "cat"]
dd_list = defaultdict(list)
for word in words:
    first_letter = word[0]
    dd_list[first_letter].append(word)
print(f"defaultdict(list) for grouping: {dd_list}")

# --- deque ---
d = deque([1, 2, 3])
print(f"\nDeque: {d}")
d.append(4)         # Add to right
d.appendleft(0)     # Add to left
print(f"After appends: {d}")
right_val = d.pop()
left_val = d.popleft()
print(f"Popped right: {right_val}, Popped left: {left_val}")
print(f"Deque after pops: {d}")