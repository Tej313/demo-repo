from collections import defaultdict

# Define the factory function
def factory(arg):
    # Do some processing here...
    result = arg.upper()
    return result

# Create a defaultdict with a lambda function as default_factory
def_dict = defaultdict(lambda: factory('default value'))

# Access a missing key and print the result
missing_key_result = def_dict['missing']
print(f"Result for 'missing': {missing_key_result}")
