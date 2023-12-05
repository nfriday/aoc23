import re

input = open("05/input.txt", "r").read().split('\n\n')

# part 1

data = [int(i) for i in re.findall('(\d+)',input[0])]

for convert in input[1:]:
    next_data = []

    for mapping in convert.splitlines()[1:]:
        destination, source, range = [int(i) for i in re.findall('\d+', mapping)]
        for x in [i for i in data if source <= i <= source+range-1]:
            data.remove(x)
            next_data.append(destination + x - source)

    for x in data:
        next_data.append(x)

    data = next_data

print(min(data))

# part 2

def get_overlapping(range1,range2):

    low1,high1 = sorted(range1)
    low2,high2 = sorted(range2)

    overlapping = [max(low1,low2), min(high1,high2)]

    if overlapping[0]>overlapping[1]:
        return ([],[range1])
    
    non_overlapping = []

    if low1 < low2:
        non_overlapping.append([low1,low2])

    if high1 > high2:
        non_overlapping.append([high2, high1])
    
    return [overlapping, non_overlapping]

data = [[int(i),int(i)+int(j)-1] for i,j in re.findall('(\d+) (\d+)',input[0])]

for convert in input[1:]:

    converted_data = []
    for mapping in convert.splitlines()[1:]:
        destination, source, range = [int(i) for i in re.findall('\d+', mapping)]

        next_data = []
        for x in data:
            overlapping, non_overlapping = get_overlapping(x, [source,source+range-1])

            if overlapping:
                converted_data.append([destination + overlapping[0] - source, destination + overlapping[1] - source])
                for i in non_overlapping: next_data.append(i)
            else:
                next_data.append(x)
        data = next_data
    
    for i in data: converted_data.append(i)

    data = converted_data
        
print(min(i[0] for i in data))

