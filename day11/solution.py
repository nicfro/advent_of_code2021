arr = []
with open('day11/input.txt') as f:
    for line in f:
        x = line.strip()
        arr.append(list(map(int, x)))

def light_adjacent(i, j):
    if i > 0:
        arr[i-1][j] += 1
        if j > 0:
            arr[i-1][j-1] += 1
        if j < len(arr[0])-1:
            arr[i-1][j+1] += 1
            
    if i < len(arr)-1:
        arr[i+1][j] += 1
        if j < len(arr)-1:
            arr[i+1][j+1] += 1
        if j > 0:
            arr[i+1][j-1] += 1
        
    if j > 0:
        arr[i][j-1] += 1
        
    if j < len(arr[0])-1:
        arr[i][j+1] += 1

def increment():
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] += 1
    return arr
    
def light_up(i, j):
    if arr[i][j] > 9 and (i,j) not in lit_step:
        lit_step.add((i,j))
        neighbours = light_adjacent(i,j)

total = 0
for step in range(300):
    increment()
    lit_step = set()

    current_lights = len(lit_step)
    stop = False

    while not stop:
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                light_up(i,j)
        new_lights = len(lit_step)
        stop = current_lights == new_lights
        current_lights = new_lights
        
    for i, j in lit_step:
        arr[i][j] = 0
    total += len(lit_step)
    
    if step+1 == 100:
        print(total)
        
    zeros = 0
    for line in arr:
        zeros += line.count(0)
    
    if zeros == len(arr)*len(arr[0]): 
        print(step+1)
        break