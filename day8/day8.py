import numpy as np

def getTreeVisibility(filename):
    with open(filename) as fin:
        lines = fin.read().strip().split()

    grid = [list(map(int, list(line))) for line in lines]
    n = len(grid)
    m = len(grid[0])
    grid = np.array(grid)

    count = 0
    for i in range(n):
        for j in range(m):
            h = grid[i, j]

            if j == 0 or np.amax(grid[i, :j]) < h:
                count += 1
            elif j == m - 1 or np.amax(grid[i, (j+1):]) < h:
                count += 1
            elif i == 0 or np.amax(grid[:i, j]) < h:
                count += 1
            elif i == n - 1 or np.amax(grid[(i+1):, j]) < h:
                count += 1
    return count

print(getTreeVisibility('data.txt'))