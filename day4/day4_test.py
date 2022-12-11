from day4 import getFullOverlapCount, getOverlapCount
import unittest

class Day4Test(unittest.TestCase):

    def test_get_max_calories(self):
        self.assertEqual(getFullOverlapCount('example.txt'), 2)
        self.assertEqual(getOverlapCount('example.txt'), 4)

if __name__ == '__main__':
    unittest.main()