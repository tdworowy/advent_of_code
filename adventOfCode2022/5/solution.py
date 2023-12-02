#     [G]         [P]         [M]
#     [V]     [M] [W] [S]     [Q]
#     [N]     [N] [G] [H]     [T] [F]
#     [J]     [W] [V] [Q] [W] [F] [P]
# [C] [H]     [T] [T] [G] [B] [Z] [B]
# [S] [W] [S] [L] [F] [B] [P] [C] [H]
# [G] [M] [Q] [S] [Z] [T] [J] [D] [S]
# [B] [T] [M] [B] [J] [C] [T] [G] [N]
#  1   2   3   4   5   6   7   8   9

crates1 = {
    "1": ["B", "G", "S", "C"],
    "2": ["T", "M", "W", "H", "J", "N", "V", "G"],
    "3": ["M", "Q", "S"],
    "4": ["B", "S", "L", "T", "W", "N", "M"],
    "5": ["J", "Z", "F", "T", "V", "G", "W", "P"],
    "6": ["C", "T", "B", "G", "Q", "H", "S"],
    "7": ["T", "J", "P", "B", "W"],
    "8": ["G", "D", "C", "Z", "F", "T", "Q", "M"],
    "9": ["N", "S", "H", "B", "P", "F"]
}
# part1
with open("input.txt.txt") as input_file:
    for line in input_file.readlines():
        print(line)
        line = line.split()

        from_ = line[3]
        to_ = line[5]
        count = int(line[1])

        crates_to_move = []
        for i in range(count):
            if crates1[from_]:
                crates_to_move.append(crates1[from_].pop())
        if crates_to_move:
            crates1[to_].extend(crates_to_move)

for k, v in crates1.items():
    print(f"{k}: {v}")

# part2
crates2 = {
    "1": ["B", "G", "S", "C"],
    "2": ["T", "M", "W", "H", "J", "N", "V", "G"],
    "3": ["M", "Q", "S"],
    "4": ["B", "S", "L", "T", "W", "N", "M"],
    "5": ["J", "Z", "F", "T", "V", "G", "W", "P"],
    "6": ["C", "T", "B", "G", "Q", "H", "S"],
    "7": ["T", "J", "P", "B", "W"],
    "8": ["G", "D", "C", "Z", "F", "T", "Q", "M"],
    "9": ["N", "S", "H", "B", "P", "F"]
}

with open("input.txt") as input_file:
    for line in input_file.readlines():
        #        print(line)
        line = line.split()

        from_ = line[3]
        to_ = line[5]
        count = int(line[1])
        crates_to_move = []
        for i in range(count):
            if crates2[from_]:
                crates_to_move.append(crates2[from_].pop())
        if crates_to_move:
            crates2[to_].extend(crates_to_move[::-1])

for k, v in crates2.items():
    print(f"{k}: {v}")
# CFFHVVHNC <- part1
# FSZWBPTBG <- part2
