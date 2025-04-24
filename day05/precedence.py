# day05/precedence.py
# Original: 10 + 5 * 8 / 4 - 1 -> 10 + 40 / 4 - 1 -> 10 + 10.0 - 1 -> 19.0
result1 = 10 + 5 * 2 ** 3 / 4 - 1
print(f"Result (default precedence): {result1}")

# With parentheses: (15) * (8) / (3) -> 120 / 3 -> 40.0
result2 = (10 + 5) * (2 ** 3) / (4 - 1)
print(f"Result (with parentheses): {result2}")