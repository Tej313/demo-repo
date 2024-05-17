from collections import defaultdict

class CustomDefaultDict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        if key not in self:
            self[key] = self.default_factory()
        print(f"Key '{key}' was missing. Added with value '{self[key]}'")
        return self[key]

def default_factory():
    return "Default Value"

# Create an instance of CustomDefaultDict with a default factory function
dd = CustomDefaultDict(default_factory)

# Accessing a missing key will trigger __missing__ to create it with the default value
print(dd['missing_key'])

# Now, accessing the same missing key again will not trigger __missing__ since it's already set
print(dd['missing_key'])

# Accessing another key that is not present will again trigger __missing__ to create it
print(dd['another_missing_key'])
