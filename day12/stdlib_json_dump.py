# day12/stdlib_json_dump.py
import json

py_dict = {
    "name": "Alice",
    "age": 30,
    "isStudent": False,
    "courses": [
        {"title": "History", "credits": 3},
        {"title": "Math", "credits": 4}
    ],
    "address": None
}

# Python dict to JSON string
json_string = json.dumps(py_dict, indent=4) 
print("JSON String:")
print(json_string)

# Python dict to JSON file
file_path = "day12/data.json"
with open(file_path, "w") as f:
    json.dump(py_dict, f, indent=4)
print(f"\nData written to {file_path}")