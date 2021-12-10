from collections import defaultdict


arr = []
with open('day8/input.txt') as f:
    for line in f:
        x = line.strip()
        arr.append(x)

part1 = {2:1,
         4:1,
         3:1,
         7:1}

part2 = defaultdict(int)
part2[2] = 1
part2[4] = 4
part2[3] = 7
part2[7] = 8

"""         
def part2(i):
    if i == 2:
        return 1
    if i == 4:
        return 4
    if i == 3:
        return 7
    if i == 7:
        return 8
    return 0
"""     

total = 0
for i in arr:
    total += sum(filter(None, [*map(part1.get, [len(x) for x in i.split("|")[1].split()])]))
print(total)


total = 0
for i in range(len(arr)):
    numbers = {}
    remaining_signal = []
    for signal in arr[i].split("|")[0].split():
        translate = part2[len(signal)]
        if translate != 0:
            numbers[translate] = set(signal)
        else:
            remaining_signal.append(set(signal))

    for signal in remaining_signal:
        if len(signal) == 5:
            if len(numbers[7] - signal) == 0:
                numbers[3] = signal
            elif len(numbers[4] - signal) == 1:
                numbers[5] = signal
            else:
                numbers[2] = signal

        if len(signal) == 6:
            if len(numbers[4] - signal) == 0:
                numbers[9] = signal
            elif len(numbers[1] - signal) == 0:
                numbers[0] = signal
            else:
                numbers[6] = signal

    string_to_number = {}
    for key in numbers:
        string_to_number["".join(sorted(numbers[key]))] = key

    final_signal = ''
    for signal in arr[i].split("|")[1].split():
        final_signal += str(string_to_number["".join(sorted(signal))])
    total += int(final_signal)

print(total)