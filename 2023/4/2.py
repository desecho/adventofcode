import re

FILENAME = 'input.txt'

game_results = {}

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
    if game_id in game_results:
        result = game_results[game_id]
    else:
        for number in numbers:
            if number in winning_numbers:
                result += 1
    final_result += result
    if game_id not in game_results:
        game_results[game_id] = result
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
    final_result += len(lines)
    while len(cards) > 0:
        card = cards[0]
        final_result = play_game(cards, card, games[card][0], games[card][1], final_result)
        cards.pop(0)
    print(final_result)
