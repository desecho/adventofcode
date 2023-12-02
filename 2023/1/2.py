FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def convert_digits(value: str):
    poss = []
    for key, digit in DIGITS.items():
        pos = value.find(key)
        if pos != -1:
            poss.append((pos, key, digit))
    poss.sort(key=lambda x: x[0])
    final_value = value
    for pos, key, digit in poss:
        final_value = final_value.replace(key, str(digit), 1)

    if final_value == value:
        return final_value

    return convert_digits(final_value)

def find_first_digit(value):
    for char in value:
        if char.isdigit():
            return char
    return -1

def find_second_digit(value):
    reversed_value = value[::-1]

    value = find_first_digit(reversed_value)
    if value == -1:
        return find_first_digit(value)
    return value

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    result = 0
    for line in lines:
        print(line)
        line = convert_digits(line)
        print(line)
        x = find_first_digit(line)
        y = find_second_digit(line)
        print(x + y)
        print()
        result += int(x + y)

    print(result)
