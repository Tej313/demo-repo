from collections import UserDict

class my_defaultdict(UserDict):
    def __init__(self, default_factory=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not callable(default_factory) and default_factory is not None:
            raise TypeError('first argument must be callable or None')
        self.default_factory = default_factory

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        if key not in self:
            self[key] = self.default_factory()
        return self[key]

# Example usage
def default_factory():
    return 'Default Value'

if __name__ == '__main__':
    # Create an instance of my_defaultdict with a default factory
    dd = my_defaultdict(default_factory)

    # Accessing a missing key will trigger __missing__ to create it with the default value
    print(dd['missing_key'])

    # Now, accessing the same missing key again will not trigger __missing__ since it's already set
    print(dd['missing_key'])

    # Accessing another key that is not present will again trigger __missing__ to create it
    print(dd['another_missing_key'])
