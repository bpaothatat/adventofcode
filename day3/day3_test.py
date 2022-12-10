from day3 import getTotalPriority, getTotalPriority2
import unittest

class Day3Test(unittest.TestCase):

    def test_get_max_calories(self):
        self.assertEqual(getTotalPriority('example.txt'), 157)
        self.assertEqual(getTotalPriority2('example.txt'), 70)

if __name__ == '__main__':
    unittest.main()