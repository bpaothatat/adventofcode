from day10 import solution_1
import unittest

class Day10Test(unittest.TestCase):
    def test_get_max_calories(self):
        self.assertEqual(solution_1('example.txt'), 13140)

if __name__ == '__main__':
    unittest.main()