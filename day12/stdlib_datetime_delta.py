from datetime import datetime, timedelta

date1 = datetime(2023, 1, 1)
date2 = datetime(2023, 1, 10, 12, 0, 0)

difference = date2 - date1
print(f"Date 1: {date1}")
print(f"Date 2: {date2}")
print(f"Difference (timedelta object): {difference}")
print(f"Difference in days: {difference.days}")
print(f"Difference in total seconds: {difference.total_seconds()}")

one_week = timedelta(days=7)
future_date = date1 + one_week
print(f"{date1} + 7 days = {future_date}")