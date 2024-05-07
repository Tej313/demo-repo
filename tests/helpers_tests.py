# helloworld/tests/helpers_tests.py
import unittest
from helloworld.helpers import helper_function

class TestHelperFunction(unittest.TestCase):
    def test_return_value(self):
        self.assertEqual(helper_function(), "This is a helper function.")

if __name__ == '__main__':
    unittest.main()
