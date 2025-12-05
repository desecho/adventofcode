FILENAME = "input.txt"

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()


# Function made with AI
def merge_ranges(ranges):
    # Sort by start value
    ranges.sort(key=lambda x: x[0])

    merged = []
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end:  # overlapping or touching
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))

    return merged


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

    ranges = merge_ranges(ranges)
    counter = 0
    for r in ranges:
        x = r[1] - r[0]
        counter += x + 1

    print(counter)
