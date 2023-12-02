import re

input = open("02/input.txt", "r").readlines()

total1 = 0
total2 = 0

for line in input:
    game_num = int(re.search('^Game (\d+):', line).group(1))
    grabs = [(int(i[0]), i[1])
             for i in re.findall('(\d+) (red|green|blue)', line)]

    max_red = max([i[0] for i in grabs if i[1] == 'red'])
    max_green = max([i[0] for i in grabs if i[1] == 'green'])
    max_blue = max([i[0] for i in grabs if i[1] == 'blue'])

    total2 += max_red * max_green * max_blue

    if max_red > 12 or max_green > 13 or max_blue > 14:
        continue

    total1 += game_num

print(total1)
print(total2)
