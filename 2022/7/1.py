import re

FILENAME = 'input0.txt'
MAX = 100000

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

cd_pattern = re.compile(r'\$ cd [a-zA-Z]+')
cd_back_pattern = re.compile(r'\$ cd \.\.')
ls_pattern = re.compile(r'(\d+) .+')


if __name__ == '__main__':
    lines = load_lines(FILENAME)
    files = []
    total = 0
    for line in lines:
        cd_match = cd_pattern.match(line)
        cd_back_match = cd_back_pattern.match(line)
        ls_match = ls_pattern.match(line)
        if cd_match:
            files_sum = sum(files)
            if files_sum <= MAX:
                total += files_sum
            files = []
        elif ls_match:
            files.append(int(ls_match.group(1)))
        elif cd_back_match:
            print(line)

    print(total)
