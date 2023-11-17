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

    sorted_calories = sorted(calories)
    print(sorted_calories[-1] + sorted_calories[-2] + sorted_calories[-3])
