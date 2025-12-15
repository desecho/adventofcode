FILENAME = "input.txt"
counter = 0

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()


def find_paths(start, links):
    global counter
    paths = links[start]
    for path in paths:
        if path == "out":
            counter += 1
            return
        else:
            find_paths(path, links)


if __name__ == "__main__":
    data = load_data()
    links = {}
    for x in data:
        key, values = x.split(': ')
        values = values.split(' ')
        links[key] = values

    find_paths("you", links)
    print(counter)
