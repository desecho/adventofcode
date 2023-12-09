import re

FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

def get_numbers(num_string):
    numbers = num_string.split(" ")
    for number in numbers:
        if number != "":
            yield int(number)

main_pattern = re.compile(r'Card +[\d]+: (.+)')


if __name__ == '__main__':
    lines = load_lines(FILENAME)
    final_result = 0
    for line in lines:
        result = 0
        main_match = main_pattern.match(line)
        game = main_match.group(1)
        win_num_string, num_string = game.split("|")
        winning_numbers = list(get_numbers(win_num_string))
        numbers = list(get_numbers(num_string))
        for number in numbers:
            if number in winning_numbers:
                if result == 0:
                    result = 1
                else:
                    result *= 2
        final_result += result
    print(final_result)
