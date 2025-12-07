FILENAME = "input.txt"


def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()


def is_valid_pos(grid, pos, v):
    size = len(grid)
    return pos[0] < size and pos[1] < size and pos[0] >= 0 and pos[1] >= 0 and grid[pos[0]][pos[1]] == v

def go(v, p, grid, found):
    if not is_valid_pos(grid, p, v):
        return
    if v == 9:
        if p not in found:
            found.append(p)
        return

    left = (p[0] - 1, p[1])
    right = (p[0] + 1, p[1])
    up = (p[0], p[1] - 1)
    down = (p[0], p[1] + 1)

    go(v + 1, left, grid, found)
    go(v + 1, right, grid, found)
    go(v + 1, up, grid, found)
    go(v + 1, down, grid, found)

def calc_score(p, grid):
    found = []
    go(0, p, grid, found)
    return len(found)


if __name__ == "__main__":
    data = load_data()
    data = [list(x) for x in data]
    grid = []
    for x in data:
        grid.append([int(z) for z in x])

    starts = []

    l = len(grid)
    for i in range(l):
        for j in range(l):
            if grid[i][j] == 0:
                starts.append((i, j))

    score = 0
    for p in starts:
        score += calc_score(p, grid)

    print(score)
