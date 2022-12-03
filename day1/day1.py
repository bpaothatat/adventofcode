def getMaxCalories(filename):
    maxCalories = 0
    with open(filename) as file:
        currentCalories = 0
        for line in file:
            if line == '\n':
                if maxCalories < currentCalories:
                    maxCalories = currentCalories
                currentCalories = 0
            else:
                currentCalories += int(line) 
    return maxCalories

print(getMaxCalories('data.txt'))