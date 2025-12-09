from copy import deepcopy
from collections import defaultdict
import math
from itertools import combinations
N = 1000

FILENAME = "input.txt"

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()

def distance(p1, p2):
    return math.sqrt(
        (p2[0] - p1[0])**2 +
        (p2[1] - p1[1])**2 +
        (p2[2] - p1[2])**2
    )

def join_lists(ls, iis):
    result = set()
    for i in iis:
        for v in ls[i]:
            result.add(v)
    ls = [x for i,x in enumerate(ls) if i not in iis]
    return ls + [list(result)]


def process_circuits(circuits):
    orig_circuits = deepcopy(circuits)
    d = defaultdict(list)
    for i, c in enumerate(circuits):
        for x in c:
            d[x].append(i)
    for k, v in d.items():
        if len(v) > 1:
            circuits = join_lists(circuits, v)
            break

    if circuits == orig_circuits:
        return circuits
    else:
        return process_circuits(circuits)


if __name__ == "__main__":
    data1 = load_data()
    data = []
    for x in data1:
        v = x.split(',')
        v = tuple([int(x) for x in v])
        data.append(v)

    distances = []
    combos = combinations(data, 2)
    for i, j in combos:
        d = distance(i, j)
        distances.append(((i, j), d))

    distances = sorted(distances, key=lambda x: x[1])
    circuits = []
    last = None
    z = False
    for x in range(len(distances)):
        v = distances[x][0]
        added = False
        for c in circuits:
            for z in c:
                if z == v[0] and v[1] not in c:
                    c.append(v[1])
                    added = True
                    last = (z, v[1])
                if z == v[1] and not added and v[0] not in c:
                    c.append(v[0])
                    added = True
                    last = (z, v[0])
                if added:
                    break
            if added:
                break
            z = True
        if not added:
            circuits.append(list(v))

        circuits = process_circuits(circuits)
        if len(circuits) == 1 and z:
            break

    print(last[0][0] * last[1][0])
