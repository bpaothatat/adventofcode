from typing import Type

class TreeNode:
    def __init__(self, is_dir: bool, name, size=None) -> None:
        self.is_dir = is_dir
        self.name = name
        self.size = size
        self.children = []
        self.parent = None

    def add_child(self, child: Type['TreeNode']):
        child.parent = self
        self.children.append(child)

    def get_size(self):
        if self.is_dir:
            total_size = 0
            for child in self.children:
                total_size += child.get_size()
            return total_size
        else:
            return self.size

    def find_subdirectories_part1(self):
        dir_sizes = 0
        if self.is_dir:
            for child in self.children:
                if child.is_dir and child.get_size() <= 100000:
                    dir_sizes += child.get_size() + child.find_subdirectories_part1()
                else:
                    dir_sizes += child.find_subdirectories_part1()
        return dir_sizes

    def find_subdirectories_part2(self, min_size):
        dir_sizes = []
        if self.is_dir:
            for child in self.children:
                if child.is_dir and child.get_size() >= min_size:
                    dir_sizes += [child.get_size()] + child.find_subdirectories_part2(min_size)
                else:
                    dir_sizes += child.find_subdirectories_part2(min_size)
        return dir_sizes

class Tree:
    def __init__(self) -> None:
        self.root = TreeNode(is_dir=True, name='root')
        self.current = self.root

    def to_root(self):
        self.current = self.root
    
    def to_parent(self):
        self.current = self.current.parent

    def to_child(self, name):
        self.current = [child for child in self.current.children if child.name == name][0]

    def add_new_child(self, child):
        self.current.add_child(child)


def generate_tree(filename: str) -> Tree:
    with open(filename) as file:
        lines = file.read().strip().split('\n')

    tree = Tree()
    i = 0
    
    while i < len(lines):
        command = lines[i]
        if command == '$ cd /':
            tree.to_root()
            i += 1
        elif command == '$ ls':
            i += 1
            command = lines[i]
            while i < len(lines) and '$' not in command:
                item_type, name = command.split(' ')
                if item_type == 'dir':
                    new_node = TreeNode(is_dir=True, name = name)
                else: 
                    new_node = TreeNode(is_dir=False, name = name, size = int(item_type))
                tree.add_new_child(new_node)
                i += 1
                if i < len(lines):
                    command = lines[i]
        elif command == '$ cd ..':
            tree.to_parent()
            i += 1
        elif '$ cd' in command:
            _, _, name = command.split(' ')
            tree.to_child(name)
            i += 1

    return tree

# tree = generate_tree('data.txt')
# print(tree.root.find_subdirectories_part1())
# total_space = 70000000
# space_needed = 30000000
# current_empty_space = 70000000 - tree.root.get_size()
# possible_dirs = tree.root.find_subdirectories_part2(space_needed - current_empty_space)
# print(possible_dirs)
# print(min(possible_dirs))