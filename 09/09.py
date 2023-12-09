import re
import math

input = open("09/input.txt", "r").readlines()

history = [[int(i) for i in re.findall("-*\d+",line)] for line in input]

# part 1

def solve(x):
    steps = [x]
    n = 0
    while [i for i in steps[n] if i]:
        steps.append([a-b for a,b in zip(steps[n][1:],steps[n])])
        n += 1
    
    while n>0:
        steps[n-1].append(steps[n-1][-1] + steps[n][-1])
        n -= 1

    return steps[0][-1]

print(sum([solve(i) for i in history]))

# part 2

print(sum([solve(i[::-1]) for i in history]))