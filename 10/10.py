input = open("10/input.txt", "r").readlines()

grid = [[col for col in row.strip()] for row in input]

def connected(coord):
    row, col = coord

    connected = []

    if 0 <= row-1 < len(grid) and 0 <= col < len(grid[0]) and grid[row-1][col] in list('|7F') and grid[row][col] in list('S|LJ'):
        connected.append((row-1,col))
    if 0 <= row+1 < len(grid) and 0 <= col < len(grid[0]) and grid[row+1][col] in list('|LJ') and grid[row][col] in list('S|7F'):
        connected.append((row+1,col))
    if 0 <= row < len(grid) and 0 <= col-1 < len(grid[0]) and grid[row][col-1] in list('-LF') and grid[row][col] in list('S-J7'):
        connected.append((row,col-1))
    if 0 <= row < len(grid) and 0 <= col+1 < len(grid[0]) and grid[row][col+1] in list('-J7') and grid[row][col] in list('S-LF'):
        connected.append((row,col+1))

    return connected

# part 1

start = [(row,i.index('S')) for row, i in enumerate(grid) if 'S' in i][0]

loop = [start, connected(start)[0]]

while next := [i for i in connected(loop[-1]) if i != loop[-2]]:
    step = next[0]
    loop.append(step)

print(len(loop) // 2)

# part 2

def print_grid(grid):
    [print(''.join(row)) for row in grid]
    print("")

egrid = [["."]*(2*len(grid[0])+1) for _ in range(2*len(grid)+1)]

for row,col in loop:
    egrid[row*2+1][col*2+1] = grid[row][col]

for a,b in zip(loop,loop[1:] + [loop[0]]):
    arow,acol = a
    brow,bcol = b
    shiftrow,shiftcol = (brow-arow,bcol-acol)
    egrid[arow*2+1+shiftrow][acol*2+1+shiftcol] = "x"

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if (row,col) not in loop: grid[row][col] = '.'

def in_bounds(coord):
    row, col = coord
    return 0 <= row < len(egrid) and 0 <= col < len(egrid[0])

def floodfill(coord):

    queue = [coord]

    while queue:
        row,col = queue.pop()

        if not in_bounds((row,col)): continue
        if egrid[row][col] != ".": continue

        egrid[row][col] = 'O'

        queue.append((row-1,col))
        queue.append((row+1,col))
        queue.append((row,col-1))
        queue.append((row,col+1))

floodfill((0,0))

for row in range(len(grid)):
    for col in range(len(grid[0])):
        grid[row][col] = egrid[row*2+1][col*2+1]

# print_grid(grid)

print(sum([len([col for col in row if col=="."]) for row in grid]))
