FILENAME = 'input.txt'

def load_lines(filename):
    with open(filename) as file:
        return file.read().splitlines()

def no_anagrams(words):
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                return False
    return True

if __name__ == '__main__':
    lines = load_lines(FILENAME)
    counter = 0
    for line in lines:
        words = line.split(" ")
        if len(words) == len(set(words)) and no_anagrams(words):
            counter += 1

    print(counter)
