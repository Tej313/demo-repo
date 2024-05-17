from collections import defaultdict

# Creating a defaultdict with a default factory list and initializing it with one key-value pair
dd = defaultdict(list, letters=['a', 'b', 'c'])

# Accessing the default factory
print(dd.default_factory)

# Printing the defaultdict
print(dd)

# Accessing a missing key (this will initialize the key with an empty list)
print(dd['numbers'])

# Printing the defaultdict after accessing the missing key
print(dd)

# Appending to the 'numbers' list
dd['numbers'].append(1)
print(dd)

# Adding multiple elements to the 'numbers' list
dd['numbers'] += [2, 3]
print(dd)
