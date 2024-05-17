class MyDict(dict):
    # Defines a new class MyDict that inherits from the built-in dict class.
    def __setitem__(self, key, value):
        # Overrides the __setitem__ method of the dict class within MyDict.
        super().__setitem__(key, None)
        # Calls the __setitem__ method of the superclass (dict) to set the value associated with the key to None.

my_dict = MyDict(first=1)
# Creates an instance of MyDict named my_dict, initializing it with a key-value pair ('first', 1).

my_dict
# Outputs the content of my_dict.

my_dict['second'] = 2
# Sets the key 'second' with value 2 in my_dict.

my_dict
# Outputs the content of my_dict.

my_dict.setdefault('third', 3)
# Calls the setdefault method on my_dict with arguments 'third' and 3.

my_dict
# Outputs the content of my_dict.
