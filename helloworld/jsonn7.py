import json
class Student:
    def __init__(self, name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['age'], data['courses'])

json_string = '{"name": "Alice", "age": 25, "courses": ["Math", "Science"]}'
data = json.loads(json_string)
student = Student.from_dict(data)
print(student.name)  # Output: Alice
