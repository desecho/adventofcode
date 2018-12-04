f = open('1.txt')
lines = f.read().splitlines()

i = 0

values = [int(x) for x in lines]

for n in values:
    i += n

# Answer 1
print(i)

#-----------------
from collections import defaultdict


def calculate():
    i = 0
    d = defaultdict(int)
    d[0] = 1
    while True:
        for x in values:
            i += x
            d[i] += 1
            if d[i] == 2:
                return i


print(calculate())