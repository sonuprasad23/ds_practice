import csv

file_path = "day12/data.csv"

try:
    with open(file_path,'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        print(f"Header: {header}")

        print("Data Rows")
        for row in csv_reader:
            print(f"{row}")

except FileNotFoundError:
    print(f"Error: {file_path} not found. Run stdlib_csv_write.py first.")
