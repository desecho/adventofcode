import re

FILENAME = 'input0.txt'

RED = 12
GREEN = 13
BLUE = 14

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

main_pattern = re.compile(r'Game ([\d]+): (.+)')
blue_pattern = re.compile(r'([\d]+): blue')
green_pattern = re.compile(r'([\d]+): green')
red_pattern = re.compile(r'([\d]+): red')

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    result = 0
    for line in lines:
        main_match = main_pattern.match(line)
        game_id = int(main_match.group(1))
        game = main_match.group(2)
        sets = game.split(";")
        blue = 0
        green = 0
        red = 0
        for set in sets:
            set = set.strip()
            balls = set.split(",")
            for ball in balls:
                ball = ball.strip()
                blue_match = blue_pattern.match(ball)
                green_match = green_pattern.match(ball)
                red_match = red_pattern.match(ball)
                if blue_match:
                    blue += int(blue_match.group(1))
                elif green_match:
                    green += int(green_match.group(1))
                elif red_match:
                    red += int(red_match.group(1))
        if blue <= BLUE and green <= GREEN and red <= RED:
            print(game_id)
            result += game_id

    print(result)
