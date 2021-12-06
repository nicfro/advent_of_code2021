from collections import defaultdict

with open('day6/input.txt') as f:
    arr = f.readline()

# solution 1 & 2
solution1 = 80
solution2 = 256

arr = [int(x) for x in arr.split(",")]

total_fish = len(arr)
days_to_hatch = [0]*9

for i in arr:
    days_to_hatch[i] +=1
    

for i in range(solution2):
    new_fish = days_to_hatch[0]
    days_to_hatch = days_to_hatch[1:]
    days_to_hatch.append(new_fish)
    days_to_hatch[6] += new_fish

    total_fish += new_fish
print(total_fish)