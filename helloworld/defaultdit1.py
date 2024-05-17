from collections import defaultdict

# Correct instantiation
def_dict = defaultdict(list)  # Pass list to .default_factory
def_dict['one'] = 1  # Add a key-value pair
def_dict['missing']  # Access a missing key returns an empty list

def_dict['another_missing'].append(4)  # Modify a missing key
print(def_dict)
