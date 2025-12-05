FILENAME = "input.txt"
THRESHOLD = 4

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()


def is_valid_pos(grid, pos):
    size = len(grid)
    return pos[0] < size and pos[1] < size and pos[0] >= 0 and pos[1] >= 0


def is_paper(grid, pos):
    if not is_valid_pos(grid, pos):
        return False

    return grid[pos[0]][pos[1]] == "@"


def is_accessible(grid, pos):
    if grid[pos[0]][pos[1]] != "@":
        return False
    counter = 0
    # left
    c = (pos[0] -1, pos[1])
    if is_paper(grid, c):
        counter += 1
    # right
    c = (pos[0] +1, pos[1])
    if is_paper(grid, c):
        counter += 1

    # up
    c = (pos[0], pos[1] -1)
    if is_paper(grid, c):
        counter += 1

    # down
    c = (pos[0], pos[1] +1)
    if is_paper(grid, c):
        counter += 1

    # left up
    c = (pos[0] -1, pos[1] - 1)
    if is_paper(grid, c):
        counter += 1

    # left down
    c = (pos[0] -1, pos[1] + 1)
    if is_paper(grid, c):
        counter += 1

    # right up
    c = (pos[0] +1, pos[1] - 1)
    if is_paper(grid, c):
        counter += 1

    # right down
    c = (pos[0] +1, pos[1] + 1)
    if is_paper(grid, c):
        counter += 1

    return counter < THRESHOLD


def calculate(grid, counter):
    counter_orig = counter
    for i in range(len(grid)):
        for j in range(len(grid)):
            if is_accessible(grid, (i, j)):
                counter += 1
                grid[i][j] = '.'

    if counter == counter_orig:
        return counter
    return calculate(grid, counter)


if __name__ == "__main__":
    data = load_data()
    grid = [list(x) for x in data]

    counter = calculate(grid, 0)
    print(counter)
