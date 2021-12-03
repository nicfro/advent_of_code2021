with open('day1/input.txt') as f:
    lines = f.readlines()

lines = [int(i.strip()) for i in lines]

'''
Part 1
count the number of times a depth measurement increases from the previous measurement.

O(n) solution
'''
current = lines[0]
counter = 0
for i in range(1, len(lines)):
    new_line = lines[i]
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
last_in_sum = lines[last_in_sum_idx]
current_sum = sum(lines[:3])
counter = 0
for i in range(3, len(lines)):
    new_sum = (current_sum - last_in_sum) + lines[i]
    if current_sum < new_sum:
        counter += 1
    current_sum = new_sum
    last_in_sum_idx += 1
    last_in_sum = lines[last_in_sum_idx]

print(counter)
