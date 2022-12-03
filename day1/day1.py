def getMaxCalories(filename):
    maxCalories = 0
    with open(filename) as file:
        currentCalories = 0
        lines = file.readlines()
        for index, line in enumerate(lines):
            if line == '\n'or index == len(lines) - 1:
                if index == len(lines) - 1:
                    currentCalories += int(line)
                if maxCalories < currentCalories:
                    maxCalories = currentCalories
                currentCalories = 0
            else:
                currentCalories += int(line) 
    return maxCalories

def getMaxCalories2(filename):
    maxCalories = 0
    secondMaxCalories = 0
    thirdMaxCalories = 0
    with open(filename) as file:
        currentCalories = 0
        lines = file.readlines()
        for index, line in enumerate(lines):
            if line == '\n' or index == len(lines) - 1:
                if index == len(lines) - 1:
                    currentCalories += int(line)
                if maxCalories < currentCalories:
                    thirdMaxCalories = secondMaxCalories
                    secondMaxCalories = maxCalories
                    maxCalories = currentCalories
                elif secondMaxCalories < currentCalories:
                    thirdMaxCalories = secondMaxCalories
                    secondMaxCalories = currentCalories
                elif thirdMaxCalories < currentCalories:
                    thirdMaxCalories = currentCalories
                currentCalories = 0
            else:
                currentCalories += int(line) 
    return maxCalories + secondMaxCalories + thirdMaxCalories


#print(getMaxCalories2('data.txt'))