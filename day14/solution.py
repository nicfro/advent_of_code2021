from LinkedList import LinkedList
from Node import Node
from collections import defaultdict
from collections import Counter
from functools import cache


"""
Part 1: Linked List
"""
with open('day14/input.txt') as f:
    polymer, instructions = f.read().split('\n\n')

instructions_dict = {}
instructions = [x.split("->") for x in instructions.split("\n")]

for key, value in instructions:
    instructions_dict[key.strip()] = value.strip()

print(instructions_dict)
print(polymer)

lst = LinkedList()
for s in polymer:
    lst.insert_at_tail(s)
lst.print_list()

for i in range(10):
    first = lst.get_head()
    second = first.next_element
    while second:
        lookup = first.data + second.data
        insert = Node(instructions_dict[lookup])
        insert.next_element = second
        first.next_element = insert

        first = second
        second = first.next_element

counter = defaultdict(int)

cur = lst.get_head()

while cur:
    counter[cur.data] += 1
    cur = cur.next_element

print(max(counter.values())-min(counter.values()))


'''
Part 2:
Cached recursion
'''
@cache
def expand(first, second, iteration=40):
    # recursion base case
    if iteration == 0: 
        return Counter()
    middle =  instructions_dict[first+second]
    # recurse
    return  Counter(middle) + expand(first, middle, iteration-1) + expand(middle, second, iteration-1)
    
# add counters together
all_counters = sum(map(expand, polymer, polymer[1:]), Counter(polymer))
print(max(all_counters.values()) - min(all_counters.values()))