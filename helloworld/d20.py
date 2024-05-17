from collections import defaultdict

lst = [1, 1, 2, 1, 2, 2, 3, 4, 3, 3, 4, 4]

# Create a defaultdict with a lambda function as default_factory
def_dict = defaultdict(lambda: 1)

# Iterate over the list and perform multiplication
for number in lst:
    print(f"Current number: {number}")
    print(f"Previous value in def_dict[{number}]: {def_dict[number]}")
    def_dict[number] *= number
    print(f"Updated value in def_dict[{number}]: {def_dict[number]}")
    print("--------------------")

print("Final defaultdict:")
print(def_dict)
