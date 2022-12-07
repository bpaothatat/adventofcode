from day3 import getTotalPriority
import unittest

class Day3Test(unittest.TestCase):

    def test_get_max_calories(self):
        self.assertEqual(getTotalPriority('example.txt'), 157)
    
if __name__ == '__main__':
    unittest.main()