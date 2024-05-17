from collections import defaultdict

# Create a defaultdict with a default factory list
dd = defaultdict(list)

# Accessing a missing key initializes it
dd['missing']

# Using .get() to access a missing key without initializing it
print(dd.get('another_missing'))

# Print the defaultdict
print(dd)
