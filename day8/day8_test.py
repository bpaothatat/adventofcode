from day8 import getPart2, getTreeVisibility
import unittest

class Day8Test(unittest.TestCase):
    def test_get_max_calories(self):
        self.assertEqual(getTreeVisibility('example.txt'), 21)
        self.assertEqual(getPart2('example.txt'), 8)

if __name__ == '__main__':
    unittest.main()