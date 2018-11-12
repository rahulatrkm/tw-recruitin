def countMatches(grid1, grid2):
    # Write your code here
    l = len(grid1)
    s = [[0]*l for _ in range(l)]
    count = 0
    for i in range(l):
        for j in range(l):
            s[i][j] = grid1[i][j] + grid2[i][j]

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
