from collections import defaultdict

# Example data retrieved from the database
data = [
    ("Sales", "John Doe"),
    ("Sales", "Martin Smith"),
    ("Accounting", "Jane Doe"),
    ("Marketing", "Elizabeth Smith"),
    ("Marketing", "Adam Doe"),
    # Add more data as needed
]

# Create a defaultdict to store departments and their employees
department_employees = defaultdict(list)

# Populate the defaultdict with the retrieved data
for department, employee in data:
    department_employees[department].append(employee)

# Print the defaultdict to see the structure
print(department_employees)
