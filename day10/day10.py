def solution_1(filename):
    with open(filename) as file:
        input = file.read().split('\n')

    instructions = []
    cycle = 1
    for line in input:
        parts = line.split(' ')
        instructions.append((cycle, 0))

        if len(parts) == 2:
            cycle += 1
            instructions.append((cycle, int(parts[1])))

        cycle += 1

    X_value = 1
    signal_strength = 0

    for instruction in instructions:
        cycle = instruction[0]
        signal_strength += X_value * cycle if cycle % 40 == 20 else 0
        X_value += instruction[1]

    return signal_strength

#print(solution_1('data.txt')))