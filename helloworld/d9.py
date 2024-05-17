from collections import defaultdict

# Example defaultdict
default_dict = defaultdict(int)
default_dict['a'] = 1
default_dict['b'] = 2

# Example standard dictionary with the same items
standard_dict = {'a': 1, 'b': 2}

# Both dictionaries should be considered equal
print(default_dict == standard_dict)  # Output: True
