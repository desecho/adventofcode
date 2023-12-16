FILENAME = 'input2.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

def count_distance(pressed, total_time):
    speed = pressed
    time = total_time - pressed
    return speed * time

def play_race(race):
    time = race[0]
    distance = race[1]
    wins = 0
    for x in range(1, time):
        if count_distance(x, time) > distance:
            wins += 1
    return wins

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    races = []
    for line in lines:
        race = line.split(" ")
        race = [int(x) for x in race]
        races.append(race)
    result = play_race(races[0])
    print(result)
