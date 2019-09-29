import unittest
from unittest import mock
from more_functions import string_functions

class testFunctions(unittest.TestCase):
    def test_multiply_string(self):
        self.assertEqual('AyahAyahAyah', string_functions.multiply_string("Ayah", 3))


if __name__ == '__main__':
    unittest.main()
