from day2 import getScore
import unittest

class Day2Test(unittest.TestCase):

    def test_get_max_calories(self):
        part1, part2 = getScore('example.txt')
        self.assertEqual(part1, 15)
        self.assertEqual(part2, 12)
    
if __name__ == '__main__':
    unittest.main()