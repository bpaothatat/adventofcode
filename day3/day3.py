def getPriority(character):
    value = ord(character)
    if value > 96:
        value -= 96
    else:
        value -= 38
    return value

def getTotalPriority(filename):
    total_score = 0
    with open(filename) as file:
        for line in file:
            start = line[:len(line)//2]
            end = line[len(line)//2:]
            for letter in start:
                if letter in end:
                    total_score += getPriority(letter)
                    break
    return total_score

def getTotalPriority2(filename):
    total_score = 0
    with open(filename) as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            intersection = set(lines[i].rstrip()) & set(lines[i +1].rstrip()) & set(lines[i+2].rstrip())
            total_score += getPriority(intersection.pop())
    return total_score

#print(getTotalPriority('data.txt'))
#print(getTotalPriority2('data.txt'))