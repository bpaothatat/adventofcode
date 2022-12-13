from day6 import getStartOfMarkers
import unittest

class Day6Test(unittest.TestCase):
    def test_get_max_calories(self):
        part1, part2 = getStartOfMarkers('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
        self.assertEqual(part1, 7)
        self.assertEqual(part2, 19)
        part1, part2 = getStartOfMarkers('bvwbjplbgvbhsrlpgdmjqwftvncz')
        self.assertEqual(part1, 5)
        self.assertEqual(part2, 23)
        part1, part2 = getStartOfMarkers('nppdvjthqldpwncqszvftbrmjlhg')
        self.assertEqual(part1, 6)
        self.assertEqual(part2, 23)
        part1, part2 = getStartOfMarkers('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
        self.assertEqual(part1, 10)
        self.assertEqual(part2, 29)
        part1, part2 = getStartOfMarkers('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
        self.assertEqual(part1, 11)
        self.assertEqual(part2, 26)

if __name__ == '__main__':
    unittest.main()