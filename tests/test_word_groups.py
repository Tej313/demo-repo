#test_words_groups.py
import unittest
from helloworld.word_groups import group_words

class TestWordGroups(unittest.TestCase):
    def test_group_words(self):
        words = ["apple", "banana", "orange", "pear", "avocado"]
        expected_output = defaultdict(list, {'a': ['apple', 'avocado'], 'b': ['banana'], 'o': ['orange'], 'p': ['pear']})
        self.assertEqual(group_words(words), expected_output)

    def test_empty_list(self):
        words = []
        self.assertEqual(group_words(words), defaultdict(list))

    def test_single_word(self):
        words = ["hello"]
        expected_output = defaultdict(list, {'h': ['hello']})
        self.assertEqual(group_words(words), expected_output)

    def test_multiple_words_same_letter(self):
        words = ["apple", "avocado", "apricot"]
        expected_output = defaultdict(list, {'a': ['apple', 'avocado', 'apricot']})
        self.assertEqual(group_words(words), expected_output)

if __name__ == '__main__':
    unittest.main()
