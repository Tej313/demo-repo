# Example data represented as a list of tuples
sales_data = [
    ('Books', [1250.00, 1300.00, 1420.00]),
    ('Tutorials', [560.00, 630.00, 750.00]),
    ('Courses', [2500.00, 2430.00, 2750.00])
]

# Initialize a dictionary to store the total sales for each product
total_sales = {}

# Calculate the total sales for each product
for product, sales in sales_data:
    total_sales[product] = sum(sales)

# Print the total sales dictionary
print(total_sales)
