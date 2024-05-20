import json

# Python data
data = {
    "name": "Alice",
    "age": 25,
    "is_student": False,
    "courses": ["Math", "Science"],
    "graduation_year": None
}

# Serialize to JSON
json_string = json.dumps(data)
print(json_string)  # {"name": "Alice", "age": 25, "is_student": false, "courses": ["Math", "Science"], "graduation_year": null}

# Deserialize back to Python
python_data = json.loads(json_string)
print(python_data)  # {'name': 'Alice', 'age': 25, 'is_student': False, 'courses': ['Math', 'Science'], 'graduation_year': None}
