from collections import defaultdict
Vector = list[int]

class Monkey:
    def __init__(self, monkey_details: str) -> None:
        parts = monkey_details.split('\n')
        self.items_inspected = 0
        self.items = [int(value) for value in parts[1].split(':')[1].split(',')]
        self.operation = parts[2].split('=')[1].strip()
        self.divisiable = int(''.join(filter(str.isdigit, parts[3])))
        self.first_monkey = int(''.join(filter(str.isdigit, parts[4])))
        self.second_monkey = int(''.join(filter(str.isdigit, parts[5])))
    
    def inspect_items(self) -> dict:
        move = defaultdict(list)
        for item in self.items:
            updated_item = self.perform_operation(item) // 3
            if updated_item % self.divisiable == 0:
                move[self.first_monkey] += [updated_item]
            else:
                move[self.second_monkey] += [updated_item]
            self.items_inspected += 1
        self.items = []
        return move
    
    def add_items(self, items: Vector) -> None:
        self.items = self.items + items

    def perform_operation(self, current_value: int) -> int: 
        if self.operation.find('old', 3) != -1:
            if '*' in self.operation:
                return current_value * current_value
            else:
                return current_value + current_value
        else:
            value = int(self.operation.split(' ')[2])
            if '*' in self.operation:
                return current_value * value
            else:
                return current_value + value

    def __str__(self) -> str:
        return str('Number of items inspected: ' + str(self.items_inspected) + '\nOperation: '+ self.operation + '\nItems: '+ str(self.items) + '\nDisiable: '+ str(self.divisiable) + '\nTrue: ' + str(self.first_monkey) + '\nFalse ' + str(self.second_monkey))

    def __repr__(self) -> str:
        return str(self)

def get_level_of_monkey_business(filename: str) -> int:   
    with open(filename) as file:
        monkeys = [Monkey(line) for line in file.read().split('\n\n')]
    for i in range(20):
        for monkey in monkeys:
            moves = monkey.inspect_items()
            for move in moves.keys():
                monkeys[move].add_items(moves[move])
    inspects = [monkey.items_inspected for monkey in monkeys]
    inspects.sort(reverse=True)
    return inspects[0] * inspects[1]


if __name__ == "__main__":
    print('Part 1:', str(get_level_of_monkey_business('data.txt')))