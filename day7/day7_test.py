from day7 import generate_tree, TreeNode
import unittest

class Day7Test(unittest.TestCase):
    def test_get_max_calories(self):
        tree = generate_tree('example.txt')
        self.assertEqual(tree.root.find_subdirectories_part1(), 95437)
        total_space = 70000000
        space_needed = 30000000
        current_empty_space = 70000000 - tree.root.get_size()
        possible_dirs = tree.root.find_subdirectories_part2(space_needed - current_empty_space)
        self.assertEqual(min(possible_dirs), 24933642)

if __name__ == '__main__':
    unittest.main()