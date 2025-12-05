FILENAME = "input0.txt"

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()


if __name__ == "__main__":
    # load data
    data = load_data()

    data1 = []
    for x in data:
        if x == "":
            break
        data1.append(x)

    # pre-process data
    ranges = []

    for x in data1:
        r1, r2 = x.split('-')
        ranges.append((int(r1), int(r2)))

    # process

    # values = set()
    # for r in ranges:
    #     for x in range(r[0], r[1] + 1):
    #         values.add(x)

    # result = len(values)
    # print(result)

    print(ranges)
