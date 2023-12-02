test_input1 = ["30373",
               "25512",
               "65332",
               "33549",
               "35390"]


def transpose(m): return [[m[j][i] for j in range(len(m))]
                          for i in range(len(m[0]))]


def check_grid_part1(grid: list[list], visible_trees: int, checked: list[tuple[int, int]]) -> tuple[
        int, list[tuple[int, int]]]:
    new_checked = []
    for i, row in enumerate(grid[1:-1], start=1):
        for j, tree in enumerate(row[1:-1], start=1):
            if tree > max(row[0:j], default=tree) or tree > max(row[j + 1:]):
                if (j, i) not in checked:
                    visible_trees += 1
                    new_checked.append((i, j))

    return visible_trees, new_checked


def solution_part1(input: list[str]) -> int:
    grid = []
    for line in input:
        grid.append([int(x) for x in line.strip()])
    visible_trees = (2 * len(grid) + 2 * (len(grid[0]))) - 4
    visible_trees, checked = check_grid_part1(grid, visible_trees, [])
    grid = transpose(grid)
    visible_trees, checked = check_grid_part1(grid, visible_trees, checked)

    return visible_trees


# TODO don't work
def check_grid_part2(grid: list[list]) -> int:
    scenic_scores = []
    for i, row in enumerate(grid):
        for j, tree in enumerate(row):
            scenic_score_left = 0
            scenic_score_right = 0
            scenic_score_up = 0
            scenic_score_down = 0

            for other_tree in reversed(row[0:j]):
                if other_tree < tree:
                    scenic_score_left += 1
                else:
                    scenic_score_left += 1
                    break

            for other_tree in row[j + 1:]:
                if other_tree < tree:
                    scenic_score_right += 1
                else:
                    scenic_score_right += 1
                    break

            for row_up in grid[i:0:-1]:
                if row_up[j] < tree:
                    scenic_score_up += 1
                else:
                    scenic_score_up += 1
                    break

            for row_down in grid[i + 1:]:
                if row_down[j] < tree:
                    scenic_score_down += 1
                else:
                    scenic_score_down += 1
                    break

            score = scenic_score_left * scenic_score_right * \
                scenic_score_up * scenic_score_down
            for row_to_print in grid:
                print(row_to_print)
            print(
                f"{tree} [{i}, {j}] [left:{scenic_score_left} right:{scenic_score_right} up:{scenic_score_up} down:{scenic_score_down} score:{score}]")
            scenic_scores.append(score)
    return max(scenic_scores)


def solution_part2(input: list[str]) -> dict[tuple[int, int]:int]:
    grid = []
    for line in input:
        grid.append([int(x) for x in line.strip()])
    return check_grid_part2(grid)


# visible_trees1 = solution_part1(test_input1)
# print(visible_trees1) #21

trees = solution_part2(test_input1)
print("---------------------------------------------")
print(trees)  # 8
#

# part1
# with open("input.txt") as input_file:
#     visible_trees = solution_part1(input_file.readlines())
#     print(visible_trees)
# 1805

# part2
with open("input.txt") as input_file:
    trees = solution_part2(input_file.readlines())
    print(trees)
# 196 incorrect
# 191 incorrect
# 200 to low
# 2162160 incorrect
# 4662684 incorrect
# 4576338 incorrect
# 4193280 incorrect
# 710600 incorrect
# 1496  incorrect
