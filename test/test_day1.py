import unittest
from day_1.day_1 import find_first_and_last_int 

# def find_first_and_last_int(code: str) -> int:
#     list_of_numbers = [char for char in code if char.isdigit()]
#     return int("".join([list_of_numbers[0], list_of_numbers[-1]]))

class TestFindFirstAndLastInt(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(find_first_and_last_int("abc123def456"), 16)

    def test_single_digit_input(self):
        self.assertEqual(find_first_and_last_int("a1b"), 11)

    def test_no_digit_input(self):
        self.assertEqual(find_first_and_last_int("abc"), 0)

if __name__ == '__main__':
    unittest.main()