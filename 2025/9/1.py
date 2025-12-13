from itertools import combinations

FILENAME = "input.txt"

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()


def get_area(p1, p2):
    return (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)


if __name__ == "__main__":
    data1 = load_data()

    data = []
    for x in data1:
        a, b = x.split(',')
        data.append((int(a),int(b)))

    combos = combinations(data, 2)

    max_area = 0
    for p1, p2 in combos:
        area = get_area(p2,p1)
        if area > max_area:
            max_area = area

    print(max_area)
