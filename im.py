def countMatches(grid1, grid2):
    # Write your code here
    r1 = dict()
    r2 = dict()
    k1 = 0
    k2 = 0
    count = 0
    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            if grid1[i][j] == 1:
                flag = 1
                for region,pos in r1.items():
                    if (abs(i-pos[0])+abs(j-pos[j])) == 1 :
                        region.append((i,j));
                        flag = 0
                if flag:
                    r1[k1] = {(i,j)}
                    k1 += 1
            if grid2[i][j] == 1:
                flag = 1
                for region,pos in r2.items():
                    if (abs(i-pos[0])+abs(j-pos[j])) == 1:
                        region.append((i,j));
                        flag = 0
                if flag:
                    r2[k2] = {(i,j)}
                    k2 += 1

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
countMatches(g1, g2)
