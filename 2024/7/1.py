from itertools import product

FILENAME = 'input0.txt'

OPERATORS = "+*"

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

def process_lines(lines):
    output = []
    for line in lines:
        result, numbers = line.split(": ")
        numbers = numbers.split(' ')
        numbers = [int(x) for x in numbers]
        output.append((int(result), numbers))
    return output


def generate_operators(n):
    return product(OPERATORS, repeat=n)


def is_valid_record(r):
    result = r[0]
    numbers = r[1]
    operators_set = generate_operators(len(numbers) - 1)
    for os in operators_set:
        for i in range(1, len(numbers)):

    print()

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    data = process_lines(lines)
    result = 0
    for r in data:
        if is_valid_record(r):
            result += r[0]

    print(result)
