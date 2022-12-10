from day4 import getOverlapCount
import unittest

class Day4Test(unittest.TestCase):

    def test_get_max_calories(self):
        self.assertEqual(getOverlapCount('example.txt'), 2)

if __name__ == '__main__':
    unittest.main()