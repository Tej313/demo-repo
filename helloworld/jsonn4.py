import json
json_string = '{"name": "Alice", "age": 25, "is_student": false, "courses": ["Math", "Science"]}'
data = json.loads(json_string)
print(data)  # Output the Python dictionary
