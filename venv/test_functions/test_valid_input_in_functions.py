import unittest
from unittest import mock
from more_functions import validate_input_in_functions

class testFunctions(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertRaises(ValueError, validate_input_in_functions.score_input("", "24", "Invalid input"))

    def test_score_input_test_score_valid(self):
        self.assertEqual("Test name: 5", validate_input_in_functions.score_input("Carl", "5", "Invalid input"))

    def test_score_input_test_score_below_range(self):
        self.assertRaises(ValueError, validate_input_in_functions.score_input("Carl,", "-1", "Invalid input"))

    def test_score_input_test_above_range(self):
        self.assertRaises(ValueError, validate_input_in_functions.score_input("Carl", "101", "Invalid input"))

    def test_score_test_non_numeric(self):
        self.assertRaises(ValueError, validate_input_in_functions.score_input("Carl", "ah", "Invalid input"))

    def test_score_input_invalid_message(self):
        self.assertEqual("Invalid input", validate_input_in_functions.score_input("", "", "Invalid input"))


if __name__ == '__main__':
    unittest.main()
