def part1(inp):
    sum = 0
    for line in inp:
        line = list(map(int, filter(lambda s: len(s) > 0, line.split(" "))))
        d = []
        d.append(line)
        while not all(list(map(lambda a: a == 0, d[-1]))):
            a = []
            for i in range(len(d[-1]) - 1):
                a.append(d[-1][i + 1] - d[-1][i])
            d.append(a)
        last = 0
        for row in reversed(d[:-1]):
            last = last + row[0]
        sum += last
    return sum


def part2(inp):
    sum = 0
    for line in inp:
        line = list(map(int, filter(lambda s: len(s) > 0, line.split(" "))))
        d = []
        d.append(line)
        while not all(list(map(lambda a: a == 0, d[-1]))):
            a = []
            for i in range(len(d[-1]) - 1):
                a.append(d[-1][i + 1] - d[-1][i])
            d.append(a)
        last = 0
        for row in reversed(d[:-1]):
            last = -last - row[0]
        sum += last
    return -sum


test_inp = None
with open("res/day09a.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))


print("TEST DAY 09:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = None
with open("res/day09.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))


print("FINAL DAY 09:")
print(part1(inp))
print(part2(inp))
