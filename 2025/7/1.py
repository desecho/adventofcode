from copy import deepcopy

FILENAME = "input.txt"
split_positions = set()

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()


def is_valid_pos(grid, pos):
    size_x = len(grid)
    size_y = len(grid[0])
    return pos[0] < size_x and pos[1] < size_y and pos[0] >= 0 and pos[1] >= 0

def process(grid):
    global splits
    original_grid = deepcopy(grid)
    lx = len(grid)
    ly = len(grid[0])
    for x in range(lx):
        for y in range(ly):
            if grid[x][y] == "S":
                grid[x+1][y] = "|"

            if grid[x][y] == "|":
                if is_valid_pos(grid, (x + 1, y)):
                    if grid[x + 1][y] == ".":
                        grid[x + 1][y] = "|"
                    elif grid[x + 1][y] == "^":
                        split_positions.add((x+1, y))
                        if is_valid_pos(grid, (x + 1, y-1)):
                            grid[x+1][y-1] = "|"
                        if is_valid_pos(grid, (x + 1, y+1)):
                            grid[x+1][y+1] = "|"

    if original_grid == grid:
        return

    return process(grid)

if __name__ == "__main__":
    data = load_data()
    data = [list(x) for x in data]

    process(data)
    print(len(split_positions))
