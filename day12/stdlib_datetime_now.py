from datetime import datetime, date, time 

now = datetime.now()
print(f"Current date and time: {now}")
print(f"Current date: {now.date()}")
print(f"Current time: {now.time()}")
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")
print(f"Hour: {now.hour}, Minute: {now.minute}, Second: {now.second}")