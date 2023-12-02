def solution(input: str, character_number: int) -> list:
    dict = {i: char for i, char in enumerate(input)}
    group = set()
    index = 0
    while True:
        for i in range(character_number):
            group.add(list(dict.values())[i])
        if len(group) == character_number:
            return list(dict.items())[0][0] + character_number
        else:
            group = set()
            del dict[index]
            index += 1


with open("input.txt") as input_file:
    input = input_file.read()
    print("Solution 1")
    print(solution(input, 4))
    print("Solution 2")
    print(solution(input, 14))
