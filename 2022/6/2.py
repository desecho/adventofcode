FILENAME = 'input.txt'

def load_line(filename):
    with open(filename) as file:
        return file.read()


def has_duplicates(token):
    token_set=set(token)
    return len(token_set) < len(token)

if __name__ == '__main__':
    line = load_line(FILENAME)
    for i in range(0, len(line)):
        if not has_duplicates(line[i:i+14]):
            print(i+14)
            break
