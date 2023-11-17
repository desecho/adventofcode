FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

# A - rock
# B - paper
# C - scissors
# X - loose
# Y - draw
# Z - win

# Rock - 1
# Paper - 2
# Scissors - 3
SCORES = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}
if __name__ == '__main__':
    sum = 0
    lines = load_lines(FILENAME)
    for line in lines:
        sum += SCORES[line]

    print(sum)
