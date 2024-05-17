from collections import defaultdict

word = "mississippi"

# Initialize a defaultdict with int as the default factory
letter_counts = defaultdict(int)

# Count the occurrences of each letter in the word
for letter in word:
    letter_counts[letter] += 1

# Print the letter_counts dictionary
print(letter_counts)
