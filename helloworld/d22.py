from collections import defaultdict  # Import defaultdict from collections
from functools import partial  # Import partial from functools

def factory(arg):
    # Do some processing here...
    result = arg.upper()  # Convert the input arg to uppercase
    return result  # Return the processed result

# Create a defaultdict with a default_factory set to a partial function
def_dict = defaultdict(partial(factory, 'default value'))

# Accessing 'missing' key for the first time, which invokes the default_factory
print(def_dict['missing'])  # Output: DEFAULT VALUE

# Change the default_factory of def_dict to another partial function
def_dict.default_factory = partial(factory, 'another default value')

# Accessing 'another_missing' key, which now uses the updated default_factory
print(def_dict['another_missing'])  # Output: ANOTHER DEFAULT VALUE
