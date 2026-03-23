FILENAME = "input.txt"

def load_data():
    with open(FILENAME) as file:
        return file.read().splitlines()

if __name__ == "__main__":
    data = load_data()
    result = 0
    for x in data:
        result += int(x) // 3 - 2

    print(result)
