def solution(input: list[str]) -> tuple[dict, dict[str, int]]:
    path = {"/": []}
    sums = {"/": 0}
    current = ["/"]
    for line in input:
        line.strip()
        line = line.split()

        if line[0] == "$":
            if line[1] == "ls":
                continue
            if line[1] == "cd" and line[2] != "..":
                current.append(line[2])
                path["".join(current)] = []
                sums["".join(current)] = 0
            else:
                current.pop()

        elif line[0] == "dir":
            path["".join(current)].append("".join(current) + line[1])
        else:
            sums["".join(current)] += int(line[0])

    total = {i: 0 for i in path}

    def searcher(i: str, searcher_result: list[int]) -> list[int]:
        if len(path[i]) > 0:
            for j in path[i]:
                searcher(j, searcher_result)
        searcher_result.append(sums[i])
        return searcher_result[:]

    for i in path:
        searcher_result = searcher(i, [])
        total[i] += sum(searcher_result)

    return total, sums


with open("input.txt") as input_file:
    total, sums = solution(input_file.readlines())

# part1
result = sum([total[i] for i in total if total[i] <= 100000])
print(result)

used_space = sum(list(sums.values()))
disc_space = 70000000
unused_space = 30000000
del_val = disc_space

# part2
for i in total:
    if (used_space - total[i]) <= (disc_space -
                                   unused_space) and total[i] < del_val:
        del_val = total[i]
print(del_val)

# 1334506 correct 1
# 7421137 correct 2
