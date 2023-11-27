FILENAME = 'input0.txt'
MAX = 100000

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    trees = []
    for line in lines:
        tree = []
        for i in range(len(line)):
            tree.append((int(line[i]), 0))
        trees.append(tree)

    # Mark trees on the edges as visible
    for i in range(0, len(trees)):
        for j in range(0, len(trees[i])):
            if i == 0 or j == 0 or i == len(trees) - 1 or j == len(trees[i]) - 1:
                trees[i][j] = (trees[i][j][0], 1)

    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[i]) - 1):
            height = trees[i][j][0]
            if height < trees[i - 1][j][0] and trees[i - 1][j][1] == 1:

    print(trees)
