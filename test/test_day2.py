import unittest
from day_2.day_2 import  main


class TestMain(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(main(), (2685, 83707))

if __name__ == "__main__":
    unittest.main()
