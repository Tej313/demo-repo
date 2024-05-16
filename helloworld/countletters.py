from collections import defaultdict

# Create a defaultdict where the default value is int (0)
letter_counts = defaultdict(int)

# Count the occurrences of each letter in a string
word = "hello"
for letter in word:
    letter_counts[letter] += 1

print(letter_counts)
