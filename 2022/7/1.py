import re

FILENAME = 'input0.txt'
MAX = 100000

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

cd_pattern = re.compile(r'\$ cd ([\/a-zA-Z]+)')
cd_back_pattern = re.compile(r'\$ cd \.\.')
ls_pattern = re.compile(r'(\d+) .+')
dir_pattern = re.compile(r'dir ([a-zA-Z]+)')

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    dir_files = {}
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
            root_dir = root_dir + "/" + dir
            if root_dir not in dirs:
                dirs[root_dir] = []
        elif ls_match:
            dirs[root_dir].append(int(ls_match.group(1)))
        elif cd_back_match:
            root_dir = "/".join(root_dir.split("/")[:-1])

    print(dirs)

    for dir in dirs:
        files = dirs[dir]
        files_sum = sum(files)
        if files_sum <= MAX:
            dir_files[dir] = files_sum
            print("total", files_sum,total)
        print("...")
        print(dir)
        print(files_sum)
        for d in dirs:
            if d in dir and d != dir and d != "//":
                print("----")
                print(d, dir)
                print(files_sum)
                files_sum += sum(dirs[d])
                print(files_sum)
                if files_sum <= MAX:
                    total += files_sum
                    print("total2", files_sum, total)
                if d in dir_files:
                    dir_files[d] = 0
    print("END")

    for dir in dir_files:
        total += dir_files[dir]

    print(dir_files)
    print(total)
