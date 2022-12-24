from day11 import get_level_of_monkey_business
import unittest

class Day8Test(unittest.TestCase):
    def test_monkey_busineess(self):
        self.assertEqual(get_level_of_monkey_business('example.txt'), 10605)

if __name__ == '__main__':
    unittest.main()