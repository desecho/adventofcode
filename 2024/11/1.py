FILENAME = "input.txt"
BLINKS = 25

def load_data():
    with open(FILENAME) as file:
        return file.read()


def transform(stone):
    if stone == 0:
        return [1]
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        half = len(stone_str) // 2
        new_stone1 = int(stone_str[:half])
        new_stone2 = int(stone_str[half:])
        return [new_stone1, new_stone2]
    return [stone * 2024]

def blink(stones):
    result = []
    for s in stones:
        result += transform(s)

    return result

if __name__ == "__main__":
    data = load_data()
    data = data.split(" ")
    data = [int(x) for x in data]

    for _ in range(BLINKS):
        data = blink(data)

    print(len(data))
