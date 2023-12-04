import re

input = open("04/input.txt", "r").readlines()

cards = []
for line in input:
    _, part2, part3 = re.match('^Card +(\d+):(.*)\|(.*)$', line).groups()
    cards.append({
        'count': 1,
        'winners': [int(i) for i in re.findall('\d+', part2)],
        'mine': [int(i) for i in re.findall('\d+', part3)],
    })

# part 1

points = sum([int(pow(2, len([i for i in card['mine'] if i in card['winners']])-1)) for card in cards])
print(points)

# part 2

for n in range(len(cards)):
   matches = len([i for i in cards[n]['mine'] if i in cards[n]['winners']])
   for x in range(matches):
       cards[n+x+1]['count'] += cards[n]['count']

total = sum([card['count'] for card in cards])

print(total)
