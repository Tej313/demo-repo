import json

data = {
    "name": "Alice",
    "age": 25,
    "is_student": False,
    "courses": ["Math", "Science"]
}

json_string = json.dumps(data)
print(json_string)  # Output the JSON string
