FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

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
        x = find_first_digit(line)
        y = find_second_digit(line)
        result += int(x + y)

    print(result)
