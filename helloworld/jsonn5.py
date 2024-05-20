import json

# Define some data (a dictionary in this case)
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Writing JSON to a file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Reading JSON from a file
with open('data.json', 'r') as file:
    data = json.load(file)
print(data)
