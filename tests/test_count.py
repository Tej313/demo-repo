import sys
import os

# Add the project root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'helloworld')))

# Now import the required modules
from helloworld.countletters import count_characters
import unittest

# Your test cases go here
class TestCharacterCount(unittest.TestCase):
    def test_count_characters(self):
        # Your assertions here
        self.assertEqual(count_characters("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})
        self.assertEqual(count_characters(""), {})
        self.assertEqual(count_characters("aaaaa"), {'a': 5})
        self.assertEqual(count_characters("aAaAa"), {'a': 3, 'A': 2})
        self.assertEqual(count_characters("123!123!"), {'1': 2, '2': 2, '3': 2, '!': 2})
        self.assertEqual(count_characters("test test"), {'t': 4, 'e': 2, 's': 2, ' ': 1})

if __name__ == '__main__':
    unittest.main()


