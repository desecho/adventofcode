import math
from itertools import combinations
N = 10

FILENAME = "input0.txt"

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()

def distance(p1, p2):
    return math.sqrt(
        (p2[0] - p1[0])**2 +
        (p2[1] - p1[1])**2 +
        (p2[2] - p1[2])**2
    )


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
    print(distances)
    circuits = []
    for x in range(N):
        v = distances[x][0]
        print(v)
        added = False
        for c in circuits:
            for z in c:
                if z == v[0] and v[1] not in c:
                    c.append(v[1])
                    added = True
                elif z == v[1] and v[0] not in c:
                    c.append(v[0])
                    added = True
                if added:
                    break
            if added:
                break
        if not added:
            circuits.append(list(v))
        print(x)
        print(circuits)
    print(circuits)


