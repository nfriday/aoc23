import re
import math

input = open("06/input.txt", "r").readlines()

times = [int(i) for i in re.findall('\d+',input[0])]
distances = [int(i) for i in re.findall('\d+',input[1])]

def solve(time,distance):
    # charge = -velocity**2 + time*velocity - distance
    rdistance = distance + 0.0000000001
    minroot, maxroot = sorted([(-time - math.sqrt(time**2 - 4 *rdistance)) / -2, (-time + math.sqrt(time**2 - 4 *rdistance)) / -2])
    mincharge = math.ceil(minroot)
    maxcharge = math.floor(maxroot)
    return (maxcharge-mincharge+1)

# part 1

total = 1
for time,distance in zip(times,distances):
    total *= solve(time,distance)

print(total)

# part 2

time = int("".join([str(i) for i in times]))
distance = int("".join([str(i) for i in distances]))
print(solve(time,distance))

