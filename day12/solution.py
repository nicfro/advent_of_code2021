from copy import copy
from collections import defaultdict, Counter

graph = defaultdict(list)

arr = []
with open('day12/input.txt') as f:
    for line in f:
        x = line.strip()
        from_node, to_node = x.split("-")
        graph[from_node].append(to_node)
        # fix starts and ends
        if from_node != "start" and to_node != "end":
            graph[to_node].append(from_node)

def can_visit_part1(node, path):
    return node not in path or node.isupper()

def can_visit_part2(node, path):
    return can_visit_part1(node,path) or max(Counter(filter(str.islower, path)).values()) == 1

def get_paths(current, path, pred):
    # Recursion base case
    if current == 'end': 
        return [path]

    # Recusion case
    res = []
    for node in graph[current]:
        if pred(node, path):
            res += get_paths(node, path + [node], pred)

    return res

print(len(get_paths("start", ["start"],can_visit_part1)))
print(len(get_paths("start", ["start"],can_visit_part2)))



