import re

input = open("03/input.txt", "r").read().splitlines()

grid = [list(line) for line in input]

numbers = []
for row, line in enumerate(input):
    for i in re.finditer('\d+', line):
        number = i.group(0)
        col = i.span()[0]
        numbers.append((number, (row, col)))


def adjacent(coord, length, grid):
    row, col = coord

    adjacent = [
        (row-1, col-1),
        (row, col-1),
        (row+1, col-1),
        (row-1, col+length),
        (row, col+length),
        (row+1, col+length),
    ]

    for i in range(length):
        adjacent.append((row-1, col+i))
        adjacent.append((row+1, col+i))

    values = [(i[0], i[1]) for i in adjacent
              if -1 not in i
              and i[0] < len(grid)
              and i[1] < len(grid[0])
              ]

    return values

# part 1


valid_numbers = [int(i[0]) for i in numbers if
                 [grid[j[0]][j[1]] for j in adjacent(i[1], len(i[0]), grid)
                  if not re.match('\d|\.', grid[j[0]][j[1]])]
                 ]

print(sum(valid_numbers))

# part 2

potential_gears = {}

for number in numbers:
    for a in adjacent(number[1], len(number[0]), grid):
        if grid[a[0]][a[1]] == '*':
            if (a[0], a[1]) in potential_gears:
                potential_gears[(a[0], a[1])].append(int(number[0]))
            else:
                potential_gears[(a[0], a[1])] = [int(number[0])]

gear_ratios = [potential_gears[k][0] * potential_gears[k][1]
               for k in potential_gears.keys() if len(potential_gears[k]) == 2]

print(sum(gear_ratios))
