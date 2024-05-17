# Initialize a dictionary
my_dict = {'key1': 'value1', 'key2': 'value2'}

# Using try-except to handle KeyError
try:
    print(my_dict['key3'])  # Accessing a missing key raises KeyError
except KeyError:
    print('Key does not exist')
