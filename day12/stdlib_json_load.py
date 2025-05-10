import json

file_path = "day12/data.json" 

try:
    with open(file_path, "r") as f:
        loaded_data = json.load(f) 

    print("Loaded Python Dictionary:")
    print(loaded_data)
    print(f"\nName: {loaded_data['name']}")
    print(f"First course title: {loaded_data['courses'][0]['title']}")

    
    json_str_sample = '{"id": 123, "item": "widget"}'
    loaded_from_str = json.loads(json_str_sample)
    print(f"\nLoaded from string: {loaded_from_str}")

except FileNotFoundError:
    print(f"Error: {file_path} not found. Run stdlib_json_dump.py first.")