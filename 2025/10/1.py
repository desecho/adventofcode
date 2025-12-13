import re

FILENAME = "input0.txt"

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()

if __name__ == "__main__":
    data = load_data()
    lights = []
    for x in data:
        results = re.findall(r"\[([\.\#]+)\]", x)
        light = []
        for char in results[0]:
            if char == '.':
                light.append(False)
            else:
                light.append(True)
        lights.append(light)

    buttons = []
    for x in data:
        sub_buttons = []
        results = re.findall(r"\(([\d,]+)\)", x)
        for r in results:
            bs = [int(x) for x in r.split(',')]
            sub_buttons.append(bs)
        buttons.append(sub_buttons)
