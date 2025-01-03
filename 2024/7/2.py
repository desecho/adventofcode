from itertools import product

FILENAME = 'input.txt'

OPERATORS = "+*|"

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
        r = numbers[0]
        for i in range(0, len(numbers) - 1):
            if os[i] == "+":
                r += numbers[i+1]
            elif os[i] == "*":
                r *= numbers[i+1]
            elif os[i] == "|":
                r = int(str(r) + str(numbers[i+1]))
        if r == result:
            return True

    return False

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    data = process_lines(lines)
    result = 0
    for r in data:
        if is_valid_record(r):
            result += r[0]

    print(result)
