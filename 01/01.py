import re

input = open("01/input.txt", "r").readlines()

# part 1

total1 = 0
for line in input:
    digits = re.findall('\d', line)
    total1 += int(digits[0] + digits[-1])

print(total1)

# part 2

numstrings = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def getdigit(x):

    try:
        digit = int(x)
    except:
        digit = numstrings[x]
    return digit


total2 = 0

for line in input:
    digits = re.findall(
        '(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)

    num = int(str(getdigit(digits[0])) + str(getdigit(digits[-1])))
    total2 += num

print(total2)
