from collections import defaultdict
import heapq as heap


arr = []
with open('day15/input.txt') as f:
    for line in f:
        x = line.strip()
        arr.append(list(map(int, x)))

width = len(arr)
height = len(arr[0])

def get_adjacent(i,j):
    res = []
    if i > 0:
        res.append((i-1,j))
    if i < width*5-1:
        res.append((i+1,j))
    if j > 0:
        res.append((i,j-1))
    if j < height*5-1:
        res.append((i,j+1))
    return res

graph = defaultdict(lambda: defaultdict(list))

for i in range(width*5):
    for j in range(height*5):
        adjacent = get_adjacent(i,j)
        temp = []
        for x,y in adjacent:
            mul = x//width + y//height
            value = mul + int(arr[x%width][y%height])
            value = value if value <= 9 else value-9
            temp.append(((x,y), value))

        graph[i][j] = temp

startingNode = (0,0)

# Initialize PQ & travel costs
priorityQueue = []
nodeCosts = defaultdict(lambda: float('inf'))
nodeCosts[startingNode] = 0
# store values in min  heap for quick retrieval 
heap.heappush(priorityQueue, (0, startingNode))

visited = set()
parentsMap = {}

while priorityQueue:
    # Pick node with shortest distance first - Greedy approach
    _, node = heap.heappop(priorityQueue)
    visited.add(node)

    for adjNode, weight in graph[node[0]][node[1]]:
        
        if adjNode in visited:
            continue

        newCost = nodeCosts[node] + weight
        if nodeCosts[adjNode] > newCost:
            parentsMap[adjNode] = node
            nodeCosts[adjNode] = newCost
            heap.heappush(priorityQueue, (newCost, adjNode))


node = (width-1, height-1)
total = 0
while node != (0,0):
    i, j = node
    total += int(arr[i][j])
    node = parentsMap[(i, j)]

# part 1
print(total)

node = ((width*5)-1, (height*5)-1)
total = 0
while node != (0,0):
    i, j = node
    value = arr[i%width][j%height]
    
    mul = i//width + j//height
    value = mul + int(arr[i%width][j%height])
    value = value if value <= 9 else value-9  

    total += value
    node = parentsMap[(i, j)]
    
# part 2
print(total)