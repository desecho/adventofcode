FILENAME = "input0.txt"

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()


class LinkedTree:
    branches = []

    def __init__(self, id, root):
        self.id = id
        self.root = root

    def add_branch(self, branch):
        self.branches.append(branch)


def find_root(data, id):
    for x in data:
        if x[0] == id:
            return x
    raise Exception('error')

def find_roots(data, id):
    roots = []
    for x in data:
        if x[0] == id:
            roots.append(x)

    assert len(roots) > 0
    return roots



if __name__ == "__main__":
    data = load_data()
    data = [x.split(')') for x in data]
    root = find_root(data, "COM")
    root = LinkedTree(root[0], None)
    roots = find_roots(root[1])
    for r in roots:
