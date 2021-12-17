# test
x1, x2, y1, y2 = 20, 30, -10, -5
# input
x1, x2, y1, y2 = 236, 262, -78, -58

points = []
for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        points.append((i,j))
        
start = (0,0)

def shoot(x, y, min_y=y1, max_x=x2):
    position = [0,0]
    highest = 0
    while position[1] > min_y and position[0] < max_x:
        position[0] += x
        position[1] += y
        if position[1] > highest:
            highest = position[1]
        x = x-1 if x > 0 else 0
        y -= 1
        if tuple(position) in points:
            return True, highest
    return False

max_y = 0
counter = 0
for i in range(x2+1):
    for j in range(y1-1,-y1+1):
        count = shoot(i,j)
        if count:
            counter += 1
            if count[1] > max_y:
                max_y = count[1]
                
print(counter, max_y)