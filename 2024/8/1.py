from collections import defaultdict
from copy import deepcopy
from itertools import combinations

FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

# Helper function
def print_grid(grid):
    for i in grid:
        print(''.join(i))

def get_diff(point1, point2):
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return (dx, dy)

def add(point1, point2):
    x = point1[0] + point2[0]
    y = point1[1] + point2[1]
    return (x, y)

def sub(point1, point2):
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]
    return (x, y)

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    grid = [list(line) for line in lines]

    # fill grid with antinodes with '.'
    grid_antinodes = deepcopy(grid)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            grid_antinodes[x][y] = '.'

    # find all nodes
    nodes = defaultdict(list)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            value = grid[x][y]
            if value != '.':
                nodes[value].append((x, y))

    for n in nodes.values():
        combos = combinations(n, 2)
        for c in combos:
            a = c[0]
            b = c[1]
            diff = get_diff(a, b)
            z1 = add(a, diff)
            z2 = add(b, diff)
            z3 = sub(a, diff)
            z4 = sub(b, diff)
            s = set()
            s.add(z1)
            s.add(z2)
            s.add(z3)
            s.add(z4)
            if a in s:
                s.remove(a)
            if b in s:
                s.remove(b)
            antinodes = list(s)
            assert len(s) == 2
            for a in antinodes:
                x, y = a
                if x < len(grid) and y< len(grid) and x >= 0 and y >= 0:
                    grid_antinodes[x][y] = "#"

    # count antinodes
    counter = 0
    for i in grid_antinodes:
        counter += i.count("#")
    print(counter)
    # print_grid(grid)
