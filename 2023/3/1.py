
FILENAME = 'input.txt'

SYMBOLS = "*#+$-/&%@%=~"

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

def enhance_lines(lines):
    output_lines = []
    lines_length = len(lines[0]) + 2
    output_lines.append("." * lines_length)
    for line in lines:
        output_lines.append("." + line + ".")
    output_lines.append("." * lines_length)
    return output_lines

def is_part_number(lines, number_tuple):
    number = number_tuple[0]
    position = number_tuple[1]
    number_length = len(str(number))
    x_pos = position[0] - number_length
    y_pos = position[1]
    potential_symbols = []
    # Check if the number is close to a symbol
    potential_symbols.append(lines[y_pos][x_pos])
    potential_symbols.append(lines[y_pos][position[0]+1])
    for i in range(number_length + 2):
        potential_symbols.append(lines[y_pos-1][x_pos+i])
        potential_symbols.append(lines[y_pos+1][x_pos+i])

    for symbol in potential_symbols:
        if symbol in SYMBOLS:
            return True
    return False

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    lines = enhance_lines(lines)
    result = 0
    numbers = []
    for i in range(len(lines)):
        line = lines[i]
        number = ""
        for j in range(len(line)):
            char = line[j]
            if char.isdigit():
                number += char
            else:
                if number != "":
                    numbers.append((int(number), (j-1, i)))
                    number = ""
            if j == len(line) - 1 and number != "":
                numbers.append((int(number), (j-1, i)))

    for number in numbers:
        if is_part_number(lines, number):
            result += number[0]
    print(result)
