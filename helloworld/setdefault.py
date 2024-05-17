# Initialize an empty dictionary
a_dict = {}

# Using setdefault to set a default value for a missing key
a_dict.setdefault('missing_key', 'default value')

# Now, accessing the key 'missing_key' should return 'default value'
print(a_dict['missing_key'])  # Output: 'default value'

# If you try to set the same key again using setdefault, it won't change the value
a_dict.setdefault('missing_key', 'another default value')

# The dictionary remains unchanged because 'missing_key' already exists
print(a_dict)  # Output: {'missing_key': 'default value'}
