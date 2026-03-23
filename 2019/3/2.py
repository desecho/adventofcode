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


def get_vector(direction):
    if direction == "R":
        vector = (1, 0)
    elif direction == "L":
        vector = (-1, 0)
    elif direction == "U":
        vector = (0, 1)
    elif direction == "D":
        vector = (0, -1)

    return vector


def wire(grid, pos, data, t, crossings):
    for x in data:
        direction = x[0]
        value = int(x[1:])
        pos = add_wire(grid, pos, direction, value, t, crossings)


def add_wire(grid, pos, direction, value, t, crossings):
    vector = get_vector(direction)
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


def follow_wire(pos, direction, value, crossing, steps):
    vector = get_vector(direction)
    for _ in range(value):
        steps += 1
        pos = calc_pos(pos, vector)
        if pos == crossing:
            return None, steps, True

    return pos, steps, False


def wire2(pos, data, crossing):
    steps = 0
    for x in data:
        direction = x[0]
        value = int(x[1:])
        pos, steps, finished = follow_wire(pos, direction, value, crossing, steps)
        if finished:
            return steps

    raise ("Error")


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
    sums = []
    for c in crossings:
        s1 = wire2(start, x1, c)
        s2 = wire2(start, x2, c)
        sums.append(s1 + s2)

    print(min(sums))
