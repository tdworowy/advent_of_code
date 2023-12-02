# X - lose
# Y - draw
# Z - win
# A Rock +1
# B Paper +2
# C scissors +3
# win +6
# draw +3

rules1 = {
    ("A", "Y"): lambda x: x + 6 + 2,
    ("B", "Z"): lambda x: x + 6 + 3,
    ("C", "X"): lambda x: x + 6 + 1,

    ("A", "X"): lambda x: x + 3 + 1,
    ("B", "Y"): lambda x: x + 3 + 2,
    ("C", "Z"): lambda x: x + 3 + 3,

    ("A", "Z"): lambda x: x + 0 + 3,
    ("B", "X"): lambda x: x + 0 + 1,
    ("C", "Y"): lambda x: x + 0 + 2,
}

rules2 = {
    ("A", "Y"): lambda x: x + 3 + 1,
    ("B", "Z"): lambda x: x + 6 + 3,
    ("C", "X"): lambda x: x + 0 + 2,

    ("A", "X"): lambda x: x + 0 + 3,
    ("B", "Y"): lambda x: x + 3 + 2,
    ("C", "Z"): lambda x: x + 6 + 1,

    ("A", "Z"): lambda x: x + 6 + 2,
    ("B", "X"): lambda x: x + 0 + 1,
    ("C", "Y"): lambda x: x + 3 + 3,
}
result = 0
with open("input.txt") as input_file:
    for line in input_file.readlines():
        line = line.split(" ")
        input_tuple = (line[0], line[1].strip())
        result = rules2[input_tuple](result)
print(result)
