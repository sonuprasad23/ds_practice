# day12/stdlib_datetime_specific.py
from datetime import datetime

specific_dt = datetime(year=2024, month=7, day=4, hour=14, minute=30, second=0)
print(f"Specific datetime: {specific_dt}")

# Formatting with strftime()
# %B: Full month name, %d: Day of month (0-padded), %Y: Year (4-digit)
# %H: Hour (24h), %M: Minute, %S: Second
formatted_str1 = specific_dt.strftime("%B %d, %Y - %H:%M:%S")
print(f"Formatted (Friendly): {formatted_str1}")

# %Y-%m-%d
formatted_str2 = specific_dt.strftime("%Y-%m-%d")
print(f"Formatted (ISO-like date): {formatted_str2}")