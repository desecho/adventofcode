import re

f = open('12.txt')
lines = f.read().splitlines()
first_line = lines[0]
lines = lines[2:]


match = re.match(r'initial state: (.+)', first_line)
initial_state = match.groups()[0]

conversions = {}

for line in lines:
    match = re.match(r'(.+?) => (.)', line)
    k, v = match.groups()
    conversions[k] = v

GENERATIONS = 20
BORDER = '...'

# We know that ..... => . from the task explanation.

# This whole piece code shouldn't probably be here but since I wrote it already I am making use of it a little.

# We want to make sure there is always ... before and after the state.
def get_state(state):
    if state[:3] != BORDER:
        return get_state('.' + state)
    if state[-3:] != BORDER:
        return get_state(state + '.')
    return state

state = initial_state
max_length = 0
for n in range(0, GENERATIONS):
    state = get_state(state)
    # We know that the first 2 chars will always be .. so we do that
    state2 = '..'
    for x in range(2, len(state) - 2):
        key = state[x - 2: x + 3]
        state2 += conversions[key]
    state = state2
    if len(state) > max_length:
        max_length = len(state)

# Now that we know the maximum length we can make sure that the overall length won't be max_length * 2 + length of the initial state
state = max_length * '.' + initial_state + max_length * '.'
for n in range(0, GENERATIONS):
    result = 0
    # We know that the first 2 chars will always be .. so we do that
    state2 = '..'
    for x in range(2, len(state) - 2):
        key = state[x - 2: x + 3]
        state2 += conversions[key]
        index = x - max_length
        if conversions[key] == '#':
            result += index
    state = state2 + '..'

print(result)