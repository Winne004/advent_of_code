import unittest
from day_1.day_1 import find_first_and_last_int, main


class TestFindFirstAndLastInt(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(find_first_and_last_int("abc123def456"), 16)

    def test_single_digit_input(self):
        self.assertEqual(find_first_and_last_int("a1b"), 11)

    def test_no_digit_input(self):
        self.assertEqual(find_first_and_last_int("abc"), 0)

    def test_main(self):
        self.assertEqual(main(),53386)


if __name__ == "__main__":
    unittest.main()
