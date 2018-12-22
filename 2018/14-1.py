f = open('14.txt')
recipes_number = int(f.read())

LAST_RECIPES_NUMBER = 10
STEP = 1
recipes = [3, 7]
elf1 = 0
elf2 = 1

def get_valid_pos(pos):
    if pos >= len(recipes):
        pos -= len(recipes)
        return get_valid_pos(pos)
    return pos

while len(recipes) < recipes_number + LAST_RECIPES_NUMBER:
    sum_ = str(recipes[elf1] + recipes[elf2])
    if len(sum_) == 2:
        recipes.append(int(sum_[0]))
        recipes.append(int(sum_[1]))
    else: # 1
        recipes.append(int(sum_))

    elf1 = get_valid_pos(recipes[elf1] + STEP + elf1)
    elf2 = get_valid_pos(recipes[elf2] + STEP + elf2)


result = recipes[recipes_number:recipes_number + 10]
answer = ''

for n in result:
    answer += str(n)
print(answer)