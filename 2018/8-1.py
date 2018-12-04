# Not solved
f = open('8.txt')
values = f.read().split(' ')
values = [int(x) for x in values]
metadata_sum = 0

while values:
    number_of_trees = values.pop(0)
    number_of_metadata = values.pop(0)
    tree_size = (len(values) - number_of_metadata) / number_of_trees
    print(tree_size)
    import sys; sys.exit()
