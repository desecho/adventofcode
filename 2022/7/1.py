import re

FILENAME = 'input.txt'
MAX = 100000

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

def add_total(total, size):
    if size <= MAX:
        total += size
    return total


cd_pattern = re.compile(r'\$ cd ([\/a-zA-Z]+)')
cd_back_pattern = re.compile(r'\$ cd \.\.')
ls_pattern = re.compile(r'(\d+) .+')
dir_pattern = re.compile(r'dir ([a-zA-Z]+)')

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    total = 0
    dirs = {}
    root_dir = ""
    dir = ""
    for line in lines:
        cd_match = cd_pattern.match(line)
        cd_back_match = cd_back_pattern.match(line)
        ls_match = ls_pattern.match(line)
        dir_match = dir_pattern.match(line)
        if cd_match:
            dir = cd_match.group(1)
            if dir == "/":
                root_dir = dir
            elif root_dir == "/":
                root_dir = root_dir + dir
            else:
                root_dir = root_dir + "/" + dir
            if root_dir not in dirs:
                dirs[root_dir] = []
        elif ls_match:
            dirs[root_dir].append(int(ls_match.group(1)))
        elif cd_back_match:
            root_dir = "/".join(root_dir.split("/")[:-1])

    for dir in dirs:
        dirs[dir] = sum(dirs[dir])

    for dir in dirs:
        for d in dirs:
            if d.startswith(dir) and d != dir and dir != "/" and d != "/":
                dirs[dir] += dirs[d]

    for dir in dirs:
        total = add_total(total, dirs[dir])
    print(total)
