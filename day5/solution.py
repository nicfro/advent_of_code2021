with open('day5/input.txt') as f:
    for line in f:
        x, y = line.strip().split("->")
        x1, y1 = x.split(",")
        x2, y2 = y.split(",")

        print(x1,y1)
        print(x2,y2)

