# Not solved.
# Here is a list of examples:
# 10 players; last marble is worth 1618 points: high score is 8317 - works
# 13 players; last marble is worth 7999 points: high score is 146373 - doesn't work
# 17 players; last marble is worth 1104 points: high score is 2764 - works
# 21 players; last marble is worth 6111 points: high score is 54718 - works
# 30 players; last marble is worth 5807 points: high score is 37305 - works


from collections import defaultdict
import re

f = open('9.txt')
value = f.read()

match = re.match(r'(\d+) players; last marble is worth (\d+) points', value)
players, end = [int(x) for x in match.groups()]

STEP1 = 2
STEP2 = 7

NUMBER = 23

seq = [0]
n = 0
current = 0
score = defaultdict(int)
player = 1
while n < end:
    n += 1
    if n % NUMBER == 0:
        score[player] += n
        to_remove_index = current - STEP2
        to_add_score = seq.pop(to_remove_index)
        score[player] += to_add_score
        current = to_remove_index
    else:
        index = current + STEP1
        if index > len(seq):
            index -= len(seq)
        seq.insert(index, n)
        current = index

    next_player = player + 1
    if next_player > players:
        next_player = 1
    player = next_player


print(max(score.values()))
# 388593 - your answer is too high
