def countMatches(grid1, grid2):
    # Write your code here
    r1 = dict()
    r2 = dict()
    k1 = 0
    k2 = 0
    count = 0
    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            if (grid1[i][j] == 1):
                f  = 1
                for reg in r1:
                    for pos in r1[reg]:
                        if (abs(pos[0] - i) + abs(pos[1] - j)) <= 1:
                            r1[reg].add((i,j))
                            f = 0
                            break
                    if f == 0:
                        break
                if f:
                    r1[k1] = {(i,j)}
                    k1 += 1
            if (grid2[i][j] == 1):
                f  = 1
                for reg in r2:
                    for pos in r2[reg]:
                        if (abs(pos[0] - i) + abs(pos[1] - j)) <= 1:
                            r2[reg].add((i,j))
                            f  = 0
                            break
                    if f == 0:
                        break
                if f:
                    r2[k2] = {(i,j)}
                    k2 += 1

    for i in range(k1):
        for j in range(k2):
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

print(countMatches(g1, g2))
