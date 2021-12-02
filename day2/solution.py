arr = []
with open('input.txt') as f:
    for line in f:
        x, y = line.strip().split(" ")
        arr.append((x, int(y)))
"""
test case

arr = [["forward", 5],
["down", 5],
["forward", 8],
["up", 3],
["down", 8],
["forward", 2]]
"""
'''
Part 1

    forward X increases the horizontal position by X units.
    down X increases the depth by X units.
    up X decreases the depth by X units.

input: direction + value
What do you get if you multiply your final horizontal position by your final depth?

O(n)
'''
horizontal = depth = aim = 0
for direction, value in arr:
    match direction:
        case "forward":
            horizontal += value
        case "up":
            depth -= value
        case "down":
            depth += value

print(depth*horizontal)


'''
Part 2

    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.

What do you get if you multiply your final horizontal position by your final depth?
'''

horizontal = depth = aim = 0
for direction, value in arr:
    match direction:
        case "forward":
            horizontal += value
            depth = depth + (aim * value)
        case "up":
            aim -= value
        case "down":
            aim += value

print(depth * horizontal)
