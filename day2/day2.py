possible_outcomes_part1 = {
    'A X': 4, 'A Y': 8, 'A Z': 3,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 7, 'C Y': 2, 'C Z': 6
}

possible_outcomes_part2 = {
    'A X': 3, 'A Y': 4, 'A Z': 8,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 2, 'C Y': 6, 'C Z': 7
}

def getScore(filename):
    part1_score = 0
    part2_score = 0
    with open(filename) as file:
        rounds = [line for line in file.read().strip().split('\n')]
        for round in rounds:
            part1_score += possible_outcomes_part1[round]
            part2_score += possible_outcomes_part2[round]
    return part1_score, part2_score

# part1, part2 = getScore('data.txt')
# print('Part 1: ' + str(part1))
# print('Part 2: ' + str(part2))


