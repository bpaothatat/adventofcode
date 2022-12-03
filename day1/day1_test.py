from day1 import getMaxCalories
import unittest

class Day1Test(unittest.TestCase):

    def test_get_max_calories(self):
        self.assertTrue(getMaxCalories('example.txt'), 24000)
    
if __name__ == '__main__':
    unittest.main()