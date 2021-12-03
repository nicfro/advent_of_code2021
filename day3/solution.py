arr = []
with open('day3/input.txt') as f:
    for line in f:
        x = line.strip()
        arr.append(x)

'''
Part 1

Considering only the first bit of each number, 
there are five 0 bits and seven 1 bits. Since the most common bit is 1, 
the first bit of the gamma rate is 1.

Epsilon rate is the least common number

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, 
then multiply them together. What is the power consumption of the submarine? 
'''

def calc_binary(arr):
    n = "".join([str(x) for x in arr])
    return int(n,2)

result = [0]*len(arr[0])

for row in arr:
    for i, value in enumerate(row):
        add = 1 if value == "1" else -1
        result[i] += add

gamma = [1 if x > 0 else 0 for x in result]
epsilon = [1 if x < 0 else 0 for x in result]

result = calc_binary(gamma) * calc_binary(epsilon)
print(result)


'''
part 2
'''
def extract_arrays(arr, idx, common):
    # recursive base case
    if len(arr) == 1: 
        return arr[0]

    ones_array =  []
    zeros_array = []
    
    # construct arrays
    for i in arr:
        ones_array.append(i) if i[idx] == "1" else zeros_array.append(i)

    # XNOR not & xor
    evaluator = not(len(ones_array) >= len(zeros_array)) ^ common

    return extract_arrays(ones_array, idx+1, common) if evaluator else extract_arrays(zeros_array, idx+1, common)
    
oxygen = extract_arrays(arr, 0, True)
co2 = extract_arrays(arr, 0, False)

result = calc_binary(oxygen) * calc_binary(co2)
print(result)
