import re

FILENAME = 'input0.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

def get_numbers(num_string):
    numbers = num_string.split(" ")
    for number in numbers:
        if number != "":
            yield int(number)

def play_game(cards, game_id, numbers, winning_numbers, final_result):
    result = 0
    for number in numbers:
        if number in winning_numbers:
            result += 1
    final_result += result
    for i in range(game_id + 1, result+game_id+1):
        cards.append(i)

    return final_result

main_pattern = re.compile(r'Card +([\d]+): (.+)')


if __name__ == '__main__':
    lines = load_lines(FILENAME)
    final_result = 0
    games = {}
    cards = []
    for line in lines:
        main_match = main_pattern.match(line)
        game_id = int(main_match.group(1))
        game = main_match.group(2)
        win_num_string, num_string = game.split("|")
        winning_numbers = list(get_numbers(win_num_string))
        numbers = list(get_numbers(num_string))
        games[game_id] = (numbers, winning_numbers)
        final_result = play_game(cards, game_id, numbers, winning_numbers, final_result)
        print(cards)

    final_result += len(lines)
    cards2 = []
    while len(cards) > 0:
        for card in cards:
            final_result = play_game(cards2, card, games[card][0], games[card][1], final_result)
            print(cards)
            # cards.pop(0)
        cards = cards2
    print(final_result)
