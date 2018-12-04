import sys
f = open('5.txt')
value = list(f.read())
value_length = len(value)

sys.setrecursionlimit(value_length)

def is_destructible(a, b):
    return a.swapcase() == b

def get_answer(start_index, value):
    for x in range(start_index, len(value)):
        if is_destructible(value[x], value[x - 1]):
            del value[x - 1]
            del value[x - 1]
            next_start_index = x - 1
            if next_start_index <= 0:
                next_start_index = 1
            return get_answer(next_start_index, value)
    return len(value)

print(get_answer(1, value))
