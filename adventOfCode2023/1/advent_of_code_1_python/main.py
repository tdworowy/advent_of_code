def part2(self, data):
    mappings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    new_data = [
        [x if (x := "".join([str(idx) for idx, val in enumerate(mappings, 1) if line[i:].startswith(val)])) else line[i]
         for i in range(len(line))] for line in data]
    return self.part1(new_data)


digits_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
sum = 0
with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        result = []
        temp = ""
        for char in line:
            temp += char
            for key in digits_map.keys():
                if key in temp:
                    result.append(key)
                    temp =temp[len(temp)-1]
            if char.isnumeric():
                result.append(char)

        first = digits_map[result[0]] if result[0] in digits_map.keys() else result[0]
        last = digits_map[result[len(result) -1]] if result[len(result) -1] in digits_map.keys() else result[len(result) -1]
      #  print(line)
      #  print(result)
      #  print(f"{first}{last}\n")
        sum +=int(f"{first}{last}")

print(sum)
