# helloworld/tests/helloworld_tests.py
import unittest
from helloworld.helloworld import main_function

class TestMainFunction(unittest.TestCase):
    def test_output(self):
        self.assertIsNone(main_function())  # Assuming main_function prints something and returns None

if __name__ == '__main__':
    unittest.main()
