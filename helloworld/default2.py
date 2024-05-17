from collections import defaultdict

# Create a defaultdict with a default factory of list
dd = defaultdict(list)

# Append 1 to the list associated with 'key'
dd['key'].append(1)
print(dd)
