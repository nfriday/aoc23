import re
import math

input = open("08/input.txt", "r").readlines()

instructions = [0 if i=='L' else 1 for i in input[0].strip()]

nodes = {}
for i in input[2:]:
    x,l,r = re.match('^(.{3}) = \((.{3}), (.{3})\)$',i).groups()
    nodes[x] = [l,r]

# part 1    

position = 'AAA'
step = 0

while position != 'ZZZ':
    instruction = instructions[step % len(instructions)]
    position = nodes[position][instruction]
    step += 1

print(step)

# part 2

for k in nodes:
    nodes[k] += [bool(re.search('A$',k)),bool(re.search('Z$',k))]

def get_distance_to_z(position):
    step = 0
    while not nodes[position][3]:
        instruction = instructions[step % len(instructions)]
        position = nodes[position][instruction]
        step += 1
    return step

position = [k for k,v in nodes.items() if v[2]]
distances = [get_distance_to_z(i) for i in position]

print(math.lcm(*distances))