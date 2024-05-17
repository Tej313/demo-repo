from collections import defaultdict

# Sample data
dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe'),
       ('Marketing', 'Adam Doe')]

# Initialize a defaultdict with set as the default_factory
dep_dd = defaultdict(set)

# Populate the defaultdict with departments and employees
for department, employee in dep:
    dep_dd[department].add(employee)

# Remove duplicates from the defaultdict
for department, employees in dep_dd.items():
    dep_dd[department] = list(employees)

# Display the cleaned-up dictionary
print(dep_dd)
