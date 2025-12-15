FILENAME = "input.txt"
counter = 0

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()


def find_paths(start, links, walked):
    global counter
    paths = links[start]
    for path in paths:
        if path == "out":
            if "dac" in walked and "fft" in walked:
                print(walked)
                counter += 1
            return
        else:
            if "dac" == path or "fft" == path:
                walked_copy = list(walked)
                walked_copy.append(path)
                find_paths(path, links, walked_copy)
            else:
                find_paths(path, links, walked)


if __name__ == "__main__":
    data = load_data()
    links = {}
    for x in data:
        key, values = x.split(': ')
        values = values.split(' ')
        links[key] = values

    find_paths("svr", links, [])
    print(counter)
