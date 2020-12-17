"""
This program reads a part of map from a file, replicates the map to infinite width 
and finds trees found on the path made by the given directions.
"""

map_file = "map.txt"
map2d = [list(line) for line in open(map_file, 'r')]

def get_tree_count(matrix, steps):
    max_rows = len(matrix)
    max_cols = len(matrix[0])-1
    steps_forward, steps_downward = steps
    tree_count = 0
    cur_row = 0
    cur_col = 0
    while cur_row < max_rows:
        if matrix[cur_row][cur_col] == '#':
            tree_count += 1
        cur_col = (cur_col + steps_forward) % max_cols
        cur_row += steps_downward
    return tree_count
    
# part 1
part1_steps = (3,1)
tree_count = get_tree_count(map2d, part1_steps)
print(tree_count)

# part 2
part2_steps = [(1,1), (3,1), (5,1), (7,1), (1,2)]
tree_count_product = 1
for steps in part2_steps:
    tree_count_product *= get_tree_count(map2d, steps)
print(tree_count_product)
