import re
from enum import Enum
import functools

input = open("07/input.txt", "r").readlines()

cards = [{'card': k[0], 'value': int(k[1])} for k in [[j for j in i.split(' ')] for i in input]]

hand_type = Enum('hand_type', ['FIVE_OAK', 'FOUR_OAK', 'FULL_HOUSE', 'THREE_OAK', 'TWO_PAIR', 'ONE_PAIR', 'HIGH_CARD'])

def get_hand_type(x,joker=False):
    units = {}
    for i in x:
        if i in units:
            units[i] += 1
        else:
            units[i] = 1

    if joker and 'J' in units:
        j = units.pop('J')
        if not len(units): units['A'] = 0
        v = list(units.values())
        k = list(units.keys())
        most = k[v.index(max(v))]
        units[most] += j

    if 5 in units.values(): return hand_type.FIVE_OAK
    if 4 in units.values(): return hand_type.FOUR_OAK
    
    pair_count = len([k for k,v in units.items() if v==2])
    if 3 in units.values():
        if pair_count == 1:
            return hand_type.FULL_HOUSE
        else:
            return hand_type.THREE_OAK
    
    if pair_count == 2: return hand_type.TWO_PAIR
    if pair_count == 1: return hand_type.ONE_PAIR

    return hand_type.HIGH_CARD

# part 1

card_face = Enum('card_face', list('AKQJT98765432'))

def compare(a,b):
    if(a['type'].value < b['type'].value): return -1
    if(a['type'].value > b['type'].value): return 1

    for i,j in zip(a['card'],b['card']):
        if card_face[i].value < card_face[j].value: return -1
        if card_face[i].value > card_face[j].value: return 1

    return 0

for card in cards:
    card['type'] = get_hand_type(card['card'])

cards.sort(key=functools.cmp_to_key(compare),reverse=True)

total = 0
for rank,card in enumerate(cards):
    total += (rank + 1) * card['value']

print(total)

# part 2

card_face_joker = Enum('card_face', list('AKQT98765432J'))

def compare_joker(a,b):
    if(a['joker_type'].value < b['joker_type'].value): return -1
    if(a['joker_type'].value > b['joker_type'].value): return 1

    for i,j in zip(a['card'],b['card']):
        if card_face_joker[i].value < card_face_joker[j].value: return -1
        if card_face_joker[i].value > card_face_joker[j].value: return 1

    return 0

for card in cards:
    card['joker_type'] = get_hand_type(card['card'],True)

cards.sort(key=functools.cmp_to_key(compare_joker),reverse=True)

for c in cards:
    print(c['card'],c['joker_type'])

total = 0
for rank,card in enumerate(cards):
    total += (rank + 1) * card['value']

print(total)
