arr = []
with open('day10/input.txt') as f:
    for line in f:
        x = line.strip()
        arr.append(x)

starts = set("{[(<")

end_map = {"}":"{",
           ")":"(",
           "]":"[",
           ">":"<"}

points1 = {")": 3,
           "]": 57,
           "}": 1197,
           ">": 25137}

points2 = {"(": 1,
           "[": 2,
           "{": 3,
           "<": 4}

total1 = 0
part2_scores = []
for s in arr:
    total2 = 0
    stack = []
    for i in s:
        if i in starts:
            stack.append(i)
        else:
            if len(stack) > 0:
                # check if last bracket matches closing one
                if stack.pop() != end_map[i]:
                    total1 += points1[i]
                    break
            # if stack is empty a beginning is missing
            else:
                total1 += points1[i]
                break
    else:
        # everything worked missing brackets in stack
        for i in reversed(stack):
            total2 *= 5
            total2 += points2[i]
        part2_scores.append(total2)

print(total1)
print(sorted(part2_scores)[len(part2_scores)//2])