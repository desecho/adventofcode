import re

FILENAME = 'input.txt'
WORD = "XMAS"
WORD_LENGTH = 4

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

def check_word(word):
    return word == WORD

def find_word(i, j, lines):
    letter1 = lines[i][j]
    n = 0
    if letter1 != "X":
        return 0

    # horizontal right
    if i + (WORD_LENGTH - 1) < len(lines):
        word = letter1 + lines[i+1][j] + lines[i+2][j] + lines[i+3][j]
        if check_word(word):
            n += 1

    # horizontal left
    if i - (WORD_LENGTH -1) >= 0:
        word = letter1 + lines[i-1][j] + lines[i-2][j] + lines[i-3][j]
        if check_word(word):
            n += 1

    # vertical down
    if j + (WORD_LENGTH -1) < len(lines):
        word = letter1 + lines[i][j+1] + lines[i][j+2] + lines[i][j+3]
        if check_word(word):
            n += 1

    # vertical up
    if j - (WORD_LENGTH -1) >= 0:
        word = letter1 + lines[i][j-1] + lines[i][j-2] + lines[i][j-3]
        if check_word(word):
            n += 1

    # diagonal down right
    if j + (WORD_LENGTH -1) < len(lines) and i + (WORD_LENGTH -1) < len(lines):
        word = letter1 + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3]
        if check_word(word):
            n += 1

    # diagonal down left
    if j - (WORD_LENGTH -1) >= 0 and i + (WORD_LENGTH -1) < len(lines):
        word = letter1 + lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3]
        if check_word(word):
            n += 1

    # diagonal up right
    if j + (WORD_LENGTH -1) < len(lines) and i - (WORD_LENGTH -1) >= 0:
        word = letter1 + lines[i-1][j+1] + lines[i-2][j+2] + lines[i-3][j+3]
        if check_word(word):
            n += 1

    # diagonal up left
    if j - (WORD_LENGTH -1) >= 0 and i - (WORD_LENGTH -1) >= 0:
        word = letter1 + lines[i-1][j-1] + lines[i-2][j-2] + lines[i-3][j-3]
        if check_word(word):
            n += 1

    return n

if __name__ == '__main__':
    lines = load_lines(FILENAME)

    result = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            result += find_word(i, j, lines)

    print(result)
