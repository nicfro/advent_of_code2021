from copy import copy

with open('day20/input.txt') as f:
    read = f.read().split('\n\n')

def depad(image, step):
    if step % 2 == 0:
        padder = "0"
    else:
        padder = "1"

    columns = list(zip(*image))

    pad = 0
    for i in image[0:3]:
        if len(set(i)) == 1 and padder in set(i):
            pad += 1
    image = image[pad:]

    pad = 0
    for i in image[len(image)-3:len(image)]:
        if len(set(i)) == 1 and padder in set(i):
            pad += 1
    if pad > 0:
        image = image[:-pad]

    pad = 0
    for i in columns[0:3]:
        if len(set(i)) == 1 and padder in set(i):
            pad += 1

    for i in range(pad):
        for row in image:
            del row[0]

    pad = 0
    for i in columns[len(columns)-3:len(columns)]:
        if len(set(i)) == 1 and padder in set(i):
            pad += 1

    for i in range(pad):
        for row in image:
            del row[-1]
            
    return image

def pad_image(image, step):
    if step % 2 == 0:
        padder = "0"
    else:
        padder = "1"
    columns = list(zip(*image))
    pads = []
    pad = 0
    for i in image[0:3]:
        if sum([int(x) for x in i]) > 0:
            pad += 1
    pads.append(pad)

    pad = 0
    for i in image[len(image)-3:len(image)]:
        if sum([int(x) for x in i]) > 0:
            pad += 1
    pads.append(pad)

    pad = 0
    for i in columns[0:3]:
        if sum([int(x) for x in i]) > 0:
            pad += 1
    pads.append(pad)

    pad = 0
    for i in columns[len(columns)-3:len(columns)]:
        if sum([int(x) for x in i]) > 0:
            pad += 1
    pads.append(pad)
    padding = max(pads)
    
    if padding > 0:
        image_len = len(image[0])+(padding*2)
        res = [[padder]*image_len]
        for i in range(padding-1):
            res.append([padder]*image_len)
        res.extend([[padder]*padding+x+[padder]*padding for x in image])
        for i in range(padding):
            res.append([padder]*image_len)
        return res
    else:
        return image

def convolve(image):
    w = len(image[0])
    h = len(image)
    result = [["0" for x in range(w)] for y in range(h)] 
    for h_idx in range(h-2):
        for w_idx in range(w-2):
            binary = image[h_idx][w_idx:w_idx+3] + image[h_idx+1][w_idx:w_idx+3] + image[h_idx+2][w_idx:w_idx+3]
            idx = int("".join(binary),2)
            result[h_idx+1][w_idx+1] = algo[idx]
    return result

def print_image(image):
    for i in ["".join([*map(reverse_map.get, x)]) for x in image]:
        print(i)
    print()

pixel_map = {".":"0",
             "#":"1"}

reverse_map = {"0": ".",
               "1": "#"}

algo = [*map(pixel_map.get, read[0])]

image = read[1].split("\n")
image = [[*map(pixel_map.get, i)] for i in image]

iterations = 50
for _ in range(iterations):
    image = pad_image(image, _)
    image = convolve(image)

    image = depad(image, _)
    #print_image(image)
    
total = 0
for i in image:
    total += sum([int(x) for x in i])
print(total)