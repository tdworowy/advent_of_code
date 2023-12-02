# part1
with open("input.txt") as input_file:
    count = 0
    for line in input_file.readlines():
        r1, r2 = line.strip().split(",")
        r1_s, r1_e = r1.split("-")
        r2_s, r2_e = r2.split("-")

        if set(range(int(r1_s), int(r1_e) + 1)).issubset(range(int(r2_s), int(r2_e) + 1)) or \
                set(range(int(r2_s), int(r2_e) + 1)).issubset(range(int(r1_s), int(r1_e) + 1)):
            count += 1
    print(count)

# part2
with open("input.txt") as input_file:
    count = 0
    for line in input_file.readlines():
        r1, r2 = line.strip().split(",")
        r1_s, r1_e = r1.split("-")
        r2_s, r2_e = r2.split("-")

        if set(range(int(r1_s), int(r1_e) + 1)
               ).intersection(range(int(r2_s), int(r2_e) + 1)):
            count += 1
    print(count)
