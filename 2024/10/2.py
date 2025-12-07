FILENAME = "input.txt"

rating = 0


def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()


def is_valid_pos(grid, pos, v):
    size = len(grid)
    return pos[0] < size and pos[1] < size and pos[0] >= 0 and pos[1] >= 0 and grid[pos[0]][pos[1]] == v

def go(v, p, grid):
    global rating
    if not is_valid_pos(grid, p, v):
        return
    if v == 9:
        rating += 1
        return

    left = (p[0] - 1, p[1])
    right = (p[0] + 1, p[1])
    up = (p[0], p[1] - 1)
    down = (p[0], p[1] + 1)

    go(v + 1, left, grid)
    go(v + 1, right, grid)
    go(v + 1, up, grid)
    go(v + 1, down, grid)

def calc_rating(p, grid):
    global rating
    rating = 0
    go(0, p, grid)
    return rating


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

    rating = 0
    for p in starts:
        rating += calc_rating(p, grid)

    print(rating)
