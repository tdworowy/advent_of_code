# for other_tree in row[j + 1:0:-1]:
#     result = other_tree >= tree and first_time_bigger_left
#     if result:
#         first_time_bigger_left = False
#     if other_tree < tree or result:
#         scenic_score_left += 1
#     if result:
#         break
#
# for other_tree in row[j + 1:]:
#     result = other_tree >= tree and first_time_bigger_right
#     if result:
#         first_time_bigger_right = False
#     if other_tree < tree or result:
#         scenic_score_right += 1
#     if result:
#         break
#
# for row_up in grid[i:0:-1]:
#     result = row_up[j] >= tree and first_time_bigger_up
#     if result:
#         first_time_bigger_up = False
#     if row_up[j] < tree or result:
#         scenic_score_up += 1
#     if result:
#         break
#
# for row_down in grid[i + 1:]:
#     result = row_down[j] >= tree and first_time_bigger_down
#     if result:
#         first_time_bigger_down = False
#     if row_down[j] < tree or result:
#         scenic_score_down += 1
#     if result:
#         break
