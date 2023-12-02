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
        result = []
        temp = ""
        for char in line:
            temp += char
            for key in digits_map.keys():
                if key in temp:
                    result.append(key)
                    temp =""
            if char.isnumeric():
                result.append(char)

        if len(result) > 1:
                  first = digits_map[result[0]] if result[0] in digits_map.keys() else result[0]
                  last = digits_map[result[len(result) -1]] if result[len(result) -1] in digits_map.keys() else result[len(result) -1]
                  sum +=int(f"{first}{last}")

print(sum)