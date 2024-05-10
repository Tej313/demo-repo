def count_characters(s):
    """
    Counts the number of times each character appears in a string.
    
    :param s: str - the string to count characters in
    :return: dict - a dictionary of characters and their counts
    """
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        # Printing the count of each character
    for char, count in char_count.items():
        print(f"'{char}' occurs {count} times.")
    return char_count

import unittest

class TestCharacterCount(unittest.TestCase):
    def test_count_characters(self):
        # Test with a normal string
        self.assertEqual(count_characters("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})
        # Test with an empty string
        self.assertEqual(count_characters(""), {})
        # Test with a string that has all the same characters
        self.assertEqual(count_characters("aaaaa"), {'a': 5})
        # Test with a mix of case sensitivity
        self.assertEqual(count_characters("aAaAa"), {'a': 3, 'A': 2})
        # Test with numbers and special characters
        self.assertEqual(count_characters("123!123!"), {'1': 2, '2': 2, '3': 2, '!': 2})
        # Test with spaces
        self.assertEqual(count_characters("test test"), {'t': 4, 'e': 2, 's': 2, ' ': 1})

if __name__ == '__main__':
    unittest.main()
