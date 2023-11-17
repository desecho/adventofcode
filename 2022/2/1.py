FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

# A - rock
# B - paper
# C - scissors
# X - rock (1)
# Y - paper (2)
# Z - scissors (3)

SCORES = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}
if __name__ == '__main__':
    sum = 0
    lines = load_lines(FILENAME)
    for line in lines:
        sum += SCORES[line]

    print(sum)
