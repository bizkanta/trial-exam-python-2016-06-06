import unittest
from work_4 import greeter

class TestGreeter(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(greeter(''), ('Hello, Mr Nobody!'))

    def test_jani(self):
        self.assertEqual(greeter('Jani'), ('Hello, Jani!'))

    def test_number(self):
        self.assertEqual(greeter('6'), ('Hello, 6!'))

if __name__ == '__main__':
    unittest.main()
