import numpy as np
def trace(i,j,grid,r,k,f):
    flag = 1
    l = len(grid)
    print(r)
    if (i < (l-2)) and (j < (l-2)) and (i > 0) and (j > 0):
        if grid[i+1][j] == 1:
            r[k].add((i+1,j))
        f[i+1][j] = 1
        if grid[i-1][j] == 1:
            r[k].add((i-1,j))
        f[i-1][j] = 1
        if grid[i][j+1] == 1:
            r[k].add((i,j+1))
        f[i][j+1] = 1
        if grid[i][j-1] == 1:
            r[k].add((i,j-1))
        f[i][j-1] = 1
    elif (i == 0) and (j < (l-2)) and (j > 0):
        if grid[i+1][j] == 1:
            r[k].add((i+1,j))
        f[i+1][j] = 1
        if grid[i][j+1] == 1:
            r[k].add((i,j+1))
        f[i][j+1] = 1
        if grid[i][j-1] == 1:
            r[k].add((i,j-1))
        f[i][j-1] = 1
    elif (j == 0) and (i < (l-2)) and (i > 0):
        if grid[i+1][j] == 1:
            r[k].add((i+1,j))
        f[i+1][j] = 1
        if grid[i-1][j] == 1:
            r[k].add((i-1,j))
        f[i-1][j] = 1
        if grid[i][j+1] == 1:
            r[k].add((i,j+1))
        f[i][j+1] = 1
    elif (i == (l-1)) and (j < (l-2)) and (j > 0):
        if grid[i-1][j] == 1:
            r[k].add((i-1,j))
        f[i-1][j] = 1
        if grid[i][j+1] == 1:
            r[k].add((i,j+1))
        f[i][j+1] = 1
        if grid[i][j-1] == 1:
            r[k].add((i,j-1))
        f[i][j-1] = 1
    elif (j == (l-1)) and (i < (l-2)) and (i > 0):
        if grid[i+1][j] == 1:
            r[k].add((i+1,j))
        f[i+1][j] = 1
        if grid[i-1][j] == 1:
            r[k].add((i-1,j))
        f[i-1][j] = 1
        if grid[i][j-1] == 1:
            r[k].add((i,j-1))
        f[i][j-1] = 1
    elif (i == 0) and (j == 0):
        if grid[i+1][j] == 1:
            r[k].add((i+1,j))
        f[i+1][j] = 1
        if grid[i][j+1] == 1:
            r[k].add((i,j+1))
        f[i][j+1] = 1
    elif (i == (l-1)) and (j == (l-1)):
        if grid[i-1][j] == 1:
            r[k].add((i-1,j))
        f[i-1][j] = 1
        if grid[i][j-1] == 1:
            r[k].add((i,j-1))
        f[i][j-1] = 1
    elif (i == 0) and (j == (l-1)):
        if grid[i+1][j] == 1:
            r[k].add((i+1,j))
        f[i+1][j] = 1
        if grid[i][j-1] == 1:
            r[k].add((i,j-1))
        f[i][j-1] = 1
    # for (l-1,0)
    else:
        print(i,j)
        if grid[i][j+1] == 1:
            r[k].add((i,j+1))
        f[i][j+1] = 1
        if grid[i-1][j] == 1:
            r[k].add((i-1,j))
        f[i-1][j] = 1
    return r,f

def countMatches(grid1, grid2):
    # Write your code here
    #print(grid1, grid2)
    f1 = np.zeros((len(grid1),len(grid1[0])), int)
    f2 = f1.copy()
    r1 = dict()
    r2 = dict()
    k1 = 0
    k2 = 0
    count = 0
    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            if (f1[i][j] == 0) and (grid1[i][j] == 1):
                k11 = k1
                f = 1
                for reg in r1:
                    if (i,j) in r1[reg]:
                        k11 = reg
                        f = 0
                        break
                if f:
                    k11 = k1
                    r1[k11] = {(i,j)}
                    k1 += 1
                print(r1[k11])
                print(r1)
                [r1,f1] = trace(i,j,grid1,r1,k11,f1)
            if (f2[i][j] == 0) and (grid2[i][j] == 1):
                k21 = k2
                f = 1
                for reg in r2:
                    if (i,j) in r2[reg]:
                        k21 = reg
                        f = 0
                        break
                if f:
                    k21 = k2
                    r2[k21] = {(i,j)}
                    k2 += 1
                [r2,f2] = trace(i,j,grid1,r2,k21,f2)
    for i in range(k1+1):
        for j in range(k2+1):
            if r1[i] == r2[j]:
                count += 1
    return count

n = int(input())
g1 = []
for _ in range(n):
    g1.append(list(map(int, input().split())))
n = int(input())
g2 = []
for _ in range(n):
    g2.append(list(map(int, input().split())))

#print(g1,g2)
countMatches(g1, g2)
