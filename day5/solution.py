from collections import Counter

part1 = Counter()
part2 = Counter()

with open('day5/test.txt') as f:
    for line in f:
        x, _, y = line.split()
        start = complex(*map(int, x.split(",")))
        end = complex(*map(int, y.split(","))) - start
        segment = int(max(abs(end.real), abs(end.imag)))

        points = [start + end * i / segment for i in range(segment + 1)]

        if end.real == 0 or end.imag == 0:
            part1.update(points)
        part2.update(points)

print(sum(v > 1 for v in part1.values()))
print(sum(v > 1 for v in part2.values()))
