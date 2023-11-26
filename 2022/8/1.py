def count_visible_trees(grid):
    rows = len(grid)
    cols = len(grid[0])

    def is_visible(tree_height, trees_in_direction):
        return all(tree < tree_height for tree in trees_in_direction)

    visible_trees = 0

    # Count visible trees in each row
    for i in range(rows):
        for j in range(cols):
            tree_height = grid[i][j]

            # Check visibility to the left
            left_trees = grid[i][:j]
            if is_visible(tree_height, left_trees):
                visible_trees += 1

            # Check visibility to the right
            right_trees = grid[i][j+1:]
            if is_visible(tree_height, right_trees):
                visible_trees += 1

    # Count visible trees in each column
    for j in range(cols):
        for i in range(rows):
            tree_height = grid[i][j]

            # Check visibility above
            above_trees = [grid[x][j] for x in range(i)]
            if is_visible(tree_height, above_trees):
                visible_trees += 1

            # Check visibility below
            below_trees = [grid[x][j] for x in range(i+1, rows)]
            if is_visible(tree_height, below_trees):
                visible_trees += 1

    return visible_trees

# Example usage:
tree_map = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0]
]

result = count_visible_trees(tree_map)
print(f"Total visible trees: {result}")
