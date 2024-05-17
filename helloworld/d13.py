# Filename: exec_time.py

# Import defaultdict from the collections module
from collections import defaultdict

# Import timeit to measure the execution time of code snippets
from timeit import timeit

# Sample data: a list of tuples containing animals and their counts
animals = [('cat', 1), ('rabbit', 2), ('cat', 3), ('dog', 4), ('dog', 1)]

# Initialize an empty standard dictionary
std_dict = dict()

# Initialize an empty defaultdict with lists as default values
def_dict = defaultdict(list)

# Define a function to group animals using a standard dictionary
def group_with_dict():
    # Loop through each animal and count in the animals list
    for animal, count in animals:
        # Use setdefault to ensure the key exists, then append the count
        std_dict.setdefault(animal, []).append(count)
    # Return the populated dictionary
    return std_dict

# Define a function to group animals using a defaultdict
def group_with_defaultdict():
    # Loop through each animal and count in the animals list
    for animal, count in animals:
        # Directly append the count to the list corresponding to the animal
        def_dict[animal].append(count)
    # Return the populated defaultdict
    return def_dict

# Measure and print the execution time of group_with_dict using timeit
print(f'dict.setdefault() takes {timeit(group_with_dict)} seconds.')

# Measure and print the execution time of group_with_defaultdict using timeit
print(f'defaultdict takes {timeit(group_with_defaultdict)} seconds.')
