from collections import defaultdict

# Example data retrieved from the company database
data = [
    ('Sales', 'John Doe'),
    ('Sales', 'Martin Smith'),
    ('Accounting', 'Jane Doe'),
    ('Marketing', 'Elizabeth Smith'),
    ('Marketing', 'Adam Doe')
]

# Initialize a defaultdict with int as the default factory
department_employee_count = defaultdict(int)

# Count the number of employees per department
for department, employee in data:
    department_employee_count[department] += 1

# Print the department_employee_count dictionary
print(department_employee_count)
