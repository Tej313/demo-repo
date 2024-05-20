import json
class Student:
    def __init__(self, name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "courses": self.courses
        }

student = Student("Alice", 25, ["Math", "Science"])

json_string = json.dumps(student.to_dict(), indent=4)
print(json_string)
