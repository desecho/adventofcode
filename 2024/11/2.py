''' Solved with a hint from AI:
Think about what you actually need to compute.
Do you really need to keep the entire list of stones, or do you only need to keep track of how many stones of each value exist?

If you stop storing stones individually and instead store counts, the running time becomes tiny and the puzzle becomes solvable.
'''

from copy import deepcopy
from collections import defaultdict

FILENAME = "input.txt"
BLINKS = 75

def load_data():
    with open(FILENAME) as file:
        return file.read()

def is_even(x):
    return len(x) % 2 == 0

def split(x):
    half = len(x) // 2
    new_stone1 = int(x[:half])
    new_stone2 = int(x[half:])
    return [new_stone1, new_stone2]

def transform(stone):
    if stone == 0:
        return [1]
    stone_str = str(stone)
    if is_even(stone_str):
        return split(stone_str)
    return [stone * 2024]

def blink(stones):
    output = deepcopy(stones)
    for s in stones:
        result = transform(s)
        output[s] -= stones[s]
        for x in result:
            output[x] += stones[s]

    return output

if __name__ == "__main__":
    data = load_data()
    data = data.split(" ")
    data = [int(x) for x in data]
    data2 = defaultdict(int)
    for x in data:
        data2[x] = 1
    for i in range(BLINKS):
        data2 = blink(data2)

    counter = 0
    for x in data2:
        counter += data2[x]

    print(counter)
