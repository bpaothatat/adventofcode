from day1 import getMaxCalories, getMaxCalories2
import unittest

class Day1Test(unittest.TestCase):

    def test_get_max_calories(self):
        self.assertEqual(getMaxCalories('example.txt'), 24000)
        self.assertEqual(getMaxCalories2('example.txt'), 45000)
    
if __name__ == '__main__':
    unittest.main()