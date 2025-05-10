# day12/stdlib_csv_write.py
import csv

header = ['Name', 'Age', 'City']
data_rows = [
    ['Alice', 30, 'New York'],
    ['Bob', 24, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]
file_path = "day12/data.csv"

with open(file_path, 'w', newline='') as csvfile: 
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header)    
    csv_writer.writerows(data_rows) 

print(f"Data written to {file_path}")