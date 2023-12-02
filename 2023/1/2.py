FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

EXTRA_DIGITS = {
    "twone": 21,
    "sevenine": 79,
    "eightwo": 82,
    "eighthree": 83,
    "threeight": 38,
    "oneight": 18,
    "fiveight": 58,
    "nineight": 98,
}

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

def convert_digits(digits, value: str):
    poss = []
    for key, digit in digits.items():
        pos = value.find(key)
        if pos != -1:
            poss.append((pos, key, digit))
    poss.sort(key=lambda x: x[0])
    final_value = value
    if len(poss) > 0:
        final_value = final_value.replace(poss[0][1], str(poss[0][2]), 1)

    if final_value == value:
        return final_value

    return convert_digits(digits, final_value)

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
        line = convert_digits(EXTRA_DIGITS, line)
        line = convert_digits(DIGITS, line)
        x = find_first_digit(line)
        y = find_second_digit(line)
        result += int(x + y)

    print(result)
