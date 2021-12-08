import math

with open('day7/input.txt') as f:
    arr = f.readline()

arr = [int(x) for x in arr.split(",")]

def get_norm_part1(x,y):
    return abs(x-y)

def get_norm_part2(x,y):
    if math.isinf(y):
        return float('inf')
    n = int(abs(x-y))
    return n*(n + 1)/2

# weiszfeld for geometric median
def getMinDistSum(positions, norm):
    curr = sum(positions) / len(positions)
    prev = float('inf')

    err = 1e-8  
    epsilon = 1e-20  
    while norm(curr, prev) > err:
        numerator = 0
        denominator = 0
        for p in positions:
            dist = norm(curr, p) + epsilon
            numerator += p / dist
            denominator += 1 / dist
        next_p = numerator/denominator
        curr, prev = next_p, curr

    min_dist = round(curr)

    total = 0
    for i in positions:
        total += norm(i, min_dist)
    return total

print(getMinDistSum(arr, get_norm_part1))
print(getMinDistSum(arr, get_norm_part2))

