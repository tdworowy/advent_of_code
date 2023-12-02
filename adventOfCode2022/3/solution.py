import string

alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
prioriteis = {
    chr: i +
    1 for (
        i,
        chr) in enumerate(
            alphabet_lower +
        alphabet_upper)}

# Part 1
with open("input.txt") as input_file:
    result = 0
    for line in input_file.readlines():
        p1, p2 = line[:len(line) // 2], line[len(line) // 2:]
        common = set.intersection(*map(set, [p1, p2]))
        result += prioriteis[common.pop()]
print(result)

# Part 2
with open("input.txt") as input_file:
    result = 0
    index = 0
    groups = []
    group = []
    for line in input_file.readlines():
        line = line.strip()
        group.append(line)
        if index == 2:
            groups.append(group)
            group = []
            index = 0

        else:
            index += 1

    for group in groups:
        common = set.intersection(*map(set, group))
        result += prioriteis[common.pop()]
print(result)
