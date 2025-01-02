import re

FILENAME = 'input.txt'

def load_text(filename):
    with open(filename) as file:
        return file.read()


def process_text(text: str):
    x1 = text.find("don't()")
    x2 = text.find("do()")
    if x2 < x1:
        text = text.replace("do()", "", 1)
        return process_text(text)
    if x1 == -1:
        return text
    text = text[0:x1] + text[x2+4:]
    return process_text(text)

if __name__ == '__main__':
    text = load_text(FILENAME)
    text = process_text(text)
    pattern = r"mul\(([\d]{1,3}),([\d]{1,3})\)"
    matches = re.findall(pattern, text)

    result = 0
    for n1, n2 in matches:
        result += int(n1) * int(n2)

    print(result)
