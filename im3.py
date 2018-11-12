import numpy as np

def trace(i,j,grid,k,f,r,level):
    #print("level",level,r,(i,j),"\n",f)
    l = len(grid)
    if (j<(l-1)):
        if (f[i][j+1] == 0):
            f[i][j+1] = 1
            if (grid[i][j+1] == '1'):
                r[k].add((i,j+1))
                [r,f] = trace(i,j+1,grid,k,f,r,1)
    if (i<(l-1)):
        if (f[i+1][j] == 0):
            f[i+1][j] = 1
            if (grid[i+1][j] == '1'):
                r[k].add((i+1,j))
                [r,f] = trace(i+1,j,grid,k,f,r,1)
    if (level != 0) and (j > 0):
        if (f[i][j-1] == 0):
            f[i][j-1] = 1
            if (grid[i][j-1] == '1'):
                r[k].add((i,j-1))
                [r,f] = trace(i,j-1,grid,k,f,r,1)
    #print(r,f)
    return [r,f]
def countMatches(grid1, grid2):
    # Write your code here
    #print(grid1, grid2)
    l = len(grid1)
    f1 = np.zeros((l,l), int)
    f2 = f1.copy()
    r1 = dict()
    r2 = dict()
    k1 = 0
    k2 = 0
    for i in range(l):
        for j in range(l):
            if (f1[i][j] == 0) and (grid1[i][j] == '1'):
                f1[i][j] = 1
                r1[k1] = {(i,j)}
                #print("r1")
                [r1,f1] = trace(i,j,grid1,k1,f1,r1,0)
                k1 += 1
            if (f2[i][j] == 0) and (grid2[i][j] == '1'):
                f2[i][j] = 1
                r2[k2] = {(i,j)}
                #print("r2")
                [r2,f2] = trace(i,j,grid2,k2,f2,r2,0)
                k2 += 1
            f1[i][j] = 1
            f2[i][j] = 1
    #print(r1,"\n",r2)
    count = 0
    for i in range(k1):
        for j in range(k2):
            if r1[i] == r2[j]:
                count += 1
    return count

grid1_count = int(input().strip())

grid1 = []

for _ in range(grid1_count):
    grid1_item = input()
    grid1.append(grid1_item)

grid2_count = int(input().strip())

grid2 = []

for _ in range(grid2_count):
    grid2_item = input()
    grid2.append(grid2_item)

print(countMatches(grid1, grid2))
