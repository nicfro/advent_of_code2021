with open('input.txt') as f:
    lines = f.readlines()

'''
Part 1
count the number of times a depth measurement increases from the previous measurement.

O(n) solution
'''
current = int(lines[0].strip())
counter = 0
for i in range(1, len(lines)):
    new_line = int(lines[i].strip())
    if current < new_line:
        counter += 1
    current = new_line

print(counter)

'''
Part 2
count the number of times the sum of measurements in a sliding window of 3 increases

O(n) solution - for any sliding window, no sum.
'''

last_in_sum_idx = 0
last_in_sum = int(lines[last_in_sum_idx].strip())
current_sum = sum([int(x.strip()) for x in lines[:3]])
counter = 0
for i in range(3, len(lines)):
    next_in_sum = int(lines[i].strip())
    new_sum = (current_sum - last_in_sum) + next_in_sum
    if current_sum < new_sum:
        counter += 1
    current_sum = new_sum
    last_in_sum_idx += 1
    last_in_sum = int(lines[last_in_sum_idx].strip())

print(counter)
