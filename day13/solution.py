with open('day13/input.txt') as f:
    dots, instructions = f.read().split('\n\n')

dots = [tuple(map(int, x.split(","))) for x in dots.split("\n")]
instructions = [x.split("=") for x in [x.split(" ")[-1] for x in instructions.split("\n")]]

def fold(fold, x, y, axis):
    return (fold-abs(x-fold), y) if axis == "x" else (x,fold-abs(y-fold))

for axis, fold_line in instructions:
    dots = set([fold(int(fold_line), x, y, axis) for x,y in set(dots)])
    print(len(dots))

for y in range(6): 
    print(*[' $'[(x,y) in dots] for x in range(40)])