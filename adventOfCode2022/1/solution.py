

with open("input.txt") as input_file:
    index = 0
    lines = input_file.readlines()
    elves = {i: 0 for i in range(lines.count("\n") + 1)}
    for line in lines:
        if line == "\n":
            index += 1
            continue
        elves[index] += int(line.strip("\n"))
    elves = {k: v for k, v in sorted(elves.items(), key=lambda item: item[1])}
    print(elves)
