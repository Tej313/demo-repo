# Initialize a dictionary with some key-value pairs
my_dict = {'key1': 'value1', 'key2': 'value2'}

# Using .get() to retrieve values
print(my_dict.get('key1'))  # Output: 'value1'
print(my_dict.get('key3'))  # Output: None

# we can also specify a default value to return if the key is missing
print(my_dict.get('key3', 'default_value'))  # Output: 'default_value'
