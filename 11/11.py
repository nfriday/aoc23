input = open("11/input.txt", "r").readlines()

grid = [[col for col in row.strip()] for row in input]

i = 0
while i < len(grid):
    if "#" not in grid[i]:
        grid[i] = ['x' for n in grid[i]]
    i += 1

i=0
while i < len(grid[1]):
    if "#" not in [row[i] for row in grid]:
        for row in grid:
            row[i] = 'x'
    i+= 1

galaxies = []
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == "#":
            galaxies.append((row,col))

def get_distance(a,b,n,grid):
    arow,acol = a
    brow,bcol = b
    startrow,endrow = sorted([arow,brow])
    startcol,endcol = sorted([acol,bcol])
    
    h = grid[startrow][startcol:endcol]
    v = [row[startcol] for row in grid[startrow:endrow]]

    return sum([1 if i != 'x' else n for i in h+v])

def solve(n):
    total = 0
    for i, a in enumerate(galaxies[:-1]):
        for b in galaxies[i+1:]:
            total += get_distance(a,b,n,grid)
    return total

# part 1

print(solve(2))

# part 2

print(solve(1000000))