string_numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}


def part1(inp):
    sum = 0
    for line in inp:
        numbers = list(map(int, filter(lambda s: s.isnumeric(), line)))
        sum += numbers[0] * 10 + numbers[-1]
    return sum


def __find_number(line, start):
    if line[start].isnumeric():
        return int(line[start])

    for number in string_numbers:
        if number in line[start : start + len(number)]:
            return string_numbers[number]

    return None


def part2(inp):
    sum = 0
    for line in inp:
        numbers = []
        for start in range(0, len(line)):
            if n := __find_number(line, start):
                numbers.append(n)
                break

        for start in range(len(line) - 1, 0, -1):
            if n := __find_number(line, start):
                numbers.append(n)
                break

        sum += numbers[0] * 10 + numbers[-1]
    return sum


inp = None
with open("res/day01.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))

print(part1(inp))
print(part2(inp))
