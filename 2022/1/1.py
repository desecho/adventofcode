FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    calories = []
    sum = 0
    for line in lines:
        if line.strip() == '':
            calories.append(sum)
            sum = 0
            continue
        sum += int(line)

    print(max(calories))
