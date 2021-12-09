arr = []
with open('day9/input.txt') as f:
    for line in f:
        x = line.strip()
        arr.append(x)

# get neighbor function
def get_adjacent(arr, i, j):
    res = []
    if i > 0:
        res.append((i-1,j))
    if i < len(arr)-1:
        res.append((i+1,j))
    if j > 0:
        res.append((i,j-1))
    if j < len(arr[0])-1:
        res.append((i,j+1))
    return res

total = 0
low_points = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < min([arr[x][y] for x,y in get_adjacent(arr,i,j)]):
            low_points.append((i,j))
            total += int(arr[i][j])+1

print(total)

basins = []
# BFS over all low points
for i in low_points:
    queue = [i]
    visited = set()

    while queue:
        i, j = queue.pop()
        visited.add((i,j))
        new_points = get_adjacent(arr, i,j)
        for i,j in new_points:
            if arr[i][j] != '9' and (i,j) not in visited:
                queue.append((i,j))

    basins.append(len(visited))

total = 1
for i in sorted(basins)[-3:]:
    total *= i
    
print(total)