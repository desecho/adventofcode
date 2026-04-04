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

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.id


def get_tree(id, trees):
    if id in trees:
        return trees[id]
    return LinkedTree(id)


def find_roots(trees, branch):
    roots = []

    root = ""
    while root is not None:
        root = branch.root
        branch = root
        if root is not None:
            roots.append(root)

    return roots

def find_first_common_root(trees, a, b):
    roots_a = find_roots(trees, a)
    roots_b = find_roots(trees, b)
    for root in roots_a:
        if root in roots_b:
            return root

    raise Exception("error")

def count_distance(trees, a, b):
    counter = 0
    roots = find_roots(trees, a)
    for r in roots:
        counter += 1
        if r == b:
            return counter

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

    you = trees['YOU'].root
    san = trees['SAN'].root

    common_root = find_first_common_root(trees, you, san)
    a = count_distance(trees, you, common_root)
    b = count_distance(trees, san, common_root)
    print(a+b)
