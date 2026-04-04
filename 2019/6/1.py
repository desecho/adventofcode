FILENAME = "input.txt"

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()


class LinkedTree:
    def __init__(self, id):
        self.id = id
        self.root = None

    def set_root(self, root):
        self.root = root

    def parent_count(self, counter = 0):
        if self.root is None:
            return counter
        else:
            counter += 1
            return self.root.parent_count(counter)


def get_tree(id, trees):
    if id in trees:
        return trees[id]
    return LinkedTree(id)


if __name__ == "__main__":
    data = load_data()
    data = [x.split(')') for x in data]
    trees = {}
    for x in data:
        root = get_tree(x[0], trees)
        branch = get_tree(x[1], trees)
        branch.set_root(root)
        trees[x[0]] = root
        trees[x[1]] = branch

    root = trees['COM']
    result = 0
    for tree in trees.values():
        result += tree.parent_count()

    print(result)
