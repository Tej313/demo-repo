# tests/test_no.py
import unittest
from helloworld.character_count import count_characters

class TestCharacterCount(unittest.TestCase):
    def test_count_characters(self):
        # Test various scenarios
        self.assertEqual(count_characters("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})
        self.assertEqual(count_characters(""), {})
        self.assertEqual(count_characters("aaaaa"), {'a': 5})
        self.assertEqual(count_characters("aAaAa"), {'a': 3, 'A': 2})
        self.assertEqual(count_characters("123!123!"), {'1': 2, '2': 2, '3': 2, '!': 2})
        self.assertEqual(count_characters("test test"), {'t': 4, 'e': 2, 's': 2, ' ': 1})

if __name__ == '__main__':
    unittest.main()
