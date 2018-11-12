def countMatches(grid1, grid2):
    #print(grid1, grid2)
    r1 = dict()
    r2 = dict()
    k1 = 0
    k2 = 0
    count = 0
    l = len(grid1)
    for i in range(l):
        for j in range(l):
            if (grid1[i][j] == '1'):
                f  = 1
                for reg in r1:
                    for pos in r1[reg]:
                        print("r1", i,j,pos)
                        if (abs(pos[0] - i) + abs(pos[1] - j)) <= 1:
                            print("r1 inside", i,j,pos)
                            r1[reg].add((i,j))
                            f = 0
                            break
                    if f == 0:
                        break
                if f:
                    r1[k1] = {(i,j)}
                    k1 += 1
                print("r1 dict", r1)
            if (grid2[i][j] == '1'):
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

    print("r1", r1)
    print("r2", r2)

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
