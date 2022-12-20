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

def getPart2(filename):
    with open(filename) as file:
        lines = file.read().strip().split()

    grid = [list(map(int, list(line))) for line in lines]

    n = len(grid)
    m = len(grid[0])

    grid = np.array(grid)

    dd = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    ans = 0
    for i in range(n):
        for j in range(m):
            h = grid[i, j]
            score = 1

            # Scan in 4 directions
            for di, dj in dd:
                ii, jj = i + di, j + dj
                dist = 0

                while (0 <= ii < n and 0 <= jj < m) and grid[ii, jj] < h:
                    dist += 1
                    ii += di
                    jj += dj

                    if (0 <= ii < n and 0 <= jj < m) and grid[ii, jj] >= h:
                        dist += 1

                score *= dist

            ans = max(ans, score)
    return ans
#print(getPart2('data.txt'))