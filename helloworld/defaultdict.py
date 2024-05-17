from collections import defaultdict

# Group words by their first letter
words = ["apple", "banana", "orange", "pear", "avocado"]

word_groups = defaultdict(list)
for word in words:
    word_groups[word[0]].append(word)

print(word_groups)  
# Output: defaultdict(<class 'list'>, {'a': ['apple', 'avocado'], 'b': ['banana'], 'o': ['orange'], 'p': ['pear']})
