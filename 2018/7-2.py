# Not solved

import copy
from collections import defaultdict
import re

f = open('7.txt')
lines = f.read().splitlines()

available_values = set()
steps = defaultdict(list)
workers = 5
step_time = 60
value_set = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
char_times = {}
for char in value_set:
    char_times[char] = step_time + value_set.index(char) + 1

for line in lines:
    match = re.match(r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.', line)
    step_requirement, step = match.groups()
    steps[step].append(step_requirement)
    available_values.add(step)
    available_values.add(step_requirement)

seconds_passed = 0
while True:


    seconds_passed += 1

# def process():
#     for char in value_set:
#         if char not in steps and char in available_values:
#             moves.append(char)
#             for c in copy.deepcopy(steps):
#                 if char in steps[c]:
#                     steps[c].remove(char)
#                 if not steps[c]:
#                     del[steps[c]]
#             value_set.remove(char)
#             available_values.remove(char)
#             return

# moves = []
# while steps or available_values:
#     process()

# print(''.join(moves))

