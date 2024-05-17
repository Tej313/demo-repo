from timeit import timeit
from collections import defaultdict

# Function to instantiate a standard dictionary
def create_dict():
    return dict()

# Function to instantiate a defaultdict
def create_defaultdict():
    return defaultdict()

# Measure and print the execution time for creating a dict
print(f'dict() takes {timeit(create_dict, number=1000000)} seconds.')

# Measure and print the execution time for creating a defaultdict
print(f'defaultdict() takes {timeit(create_defaultdict, number=1000000)} seconds.')
