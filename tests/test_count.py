import unittest
from collections import defaultdict
from helloworld.countletters import count_characters

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

