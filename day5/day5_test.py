from day5 import getCargoTop
import unittest

class Day5Test(unittest.TestCase):

    def test_get_max_calories(self):
        part1, part2 = getCargoTop('example.txt')
        self.assertEqual(part1, 'CMZ')
        self.assertEqual(part2, 'MCD')

if __name__ == '__main__':
    unittest.main()