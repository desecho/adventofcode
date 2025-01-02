import re

FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

def check_word(word):
    return word == "MAS" or word == "SAM"

def is_border(i, j, n):
    if i == 0 or j == 0:
        return True
    if i == n - 1 or j == n - 1:
        return True
    return False

def find_x(i, j, lines):
    center = lines[i][j]
    if center != "A":
        return False

    if is_border(i,j, len(lines)):
        return False

    # \
    word1 =  lines[i-1][j-1] + "A" + lines[i+1][j+1]

    # /
    word2 =  lines[i-1][j+1] + "A" + lines[i+1][j-1]

    if check_word(word1) and check_word(word2):
        return True

    return False

if __name__ == '__main__':
    lines = load_lines(FILENAME)

    result = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            if find_x(i, j, lines):
                result += 1

    print(result)
