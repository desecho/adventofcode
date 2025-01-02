import re

FILENAME = 'input.txt'

def load_text(filename):
    with open(filename) as file:
        return file.read()

if __name__ == '__main__':
    text = load_text(FILENAME)

    pattern = r"mul\(([\d]{1,3}),([\d]{1,3})\)"
    matches = re.findall(pattern, text)

    result = 0
    for n1, n2 in matches:
        result += int(n1) * int(n2)

    print(result)
