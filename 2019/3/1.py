import math

FILENAME = "input.txt"


def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()


# Written with AI
def set_cell(grid: dict, i, j, value):
    if value == 0:
        grid.pop((i, j), None)
    else:
        grid[(i, j)] = value


# Written with AI
def get_cell(grid, i, j):
    return grid.get((i, j), 0)


def calc_pos(pos, vector):
    x = pos[0] + vector[0]
    y = pos[1] + vector[1]
    return (x, y)


def add_wire(grid, pos, direction, value, t, crossings):
    if direction == "R":
        vector = (1, 0)
    elif direction == "L":
        vector = (-1, 0)
    elif direction == "U":
        vector = (0, 1)
    elif direction == "D":
        vector = (0, -1)

    for _ in range(value):
        pos = calc_pos(pos, vector)
        x, y = pos
        grid_value = get_cell(grid, x, y)

        if grid_value == 0:
            set_cell(grid, x, y, t)
        elif grid_value == 1 and t != 1:
            set_cell(grid, x, y, "x")
            crossings.append((x, y))

    return pos


def calc_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def wire(grid, pos, data, t, crossings):
    for x in data:
        direction = x[0]
        value = int(x[1:])
        pos = add_wire(grid, pos, direction, value, t, crossings)


if __name__ == "__main__":
    data = load_data()
    x1 = data[0]
    x2 = data[1]
    x1 = x1.split(",")
    x2 = x2.split(",")
    grid = {}
    start = (0, 0)
    crossings = []
    wire(grid, start, x1, 1, crossings)
    wire(grid, start, x2, 2, crossings)

    min_dist = math.inf
    for c in crossings:
        d = calc_dist(c, start)
        if d < min_dist:
            min_dist = d

    print(min_dist)
