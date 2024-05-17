from collections import defaultdict

# Creating a standard dictionary
std_dict = dict(numbers=[1, 2, 3], letters=['a', 'b', 'c'])
print(std_dict)

# Creating a defaultdict with the same items
def_dict = defaultdict(list, numbers=[1, 2, 3], letters=['a', 'b', 'c'])
print(def_dict)

# Comparing the two dictionaries
print(std_dict == def_dict)  # Output: True
