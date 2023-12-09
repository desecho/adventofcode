import re

FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

main_pattern = re.compile(r'Card [\d]+: (.+) | (.+)')


if __name__ == '__main__':
    lines = load_lines(FILENAME)
    result = 0
    for line in lines:
        main_match = main_pattern.match(line)
        print(main_match.group(1))
        print(main_match.group(2))

    print(result)
