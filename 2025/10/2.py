from itertools import combinations
import re

FILENAME = "input0.txt"

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()

def simulate(light, combos):
    for combo in combos:
        test = [False for _ in light]
        for button in combo:
            r = []
            for i,x in enumerate(test):
                if i in button:
                    r.append(not(x))
                else:
                    r.append(x)
            test = r
            if test == light:
                return True

def process(light, buttons):
    for i in range(1, 10):
        combos = combinations(buttons, i)
        if simulate(light, combos):
            return i

if __name__ == "__main__":
    data = load_data()
    buttons = []
    for x in data:
        sub_buttons = []
        results = re.findall(r"\(([\d,]+)\)", x)
        for r in results:
            bs = [int(x) for x in r.split(',')]
            sub_buttons.append(bs)
        buttons.append(sub_buttons)

    joltages = []
    for x in data:
        results = re.findall(r"\{([\d,]+)\}", x)
        for r in results:
            js = [int(x) for x in r.split(',')]
        joltages.append(js)
