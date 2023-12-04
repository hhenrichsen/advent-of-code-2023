from util import (
    AfterRegion,
    InputParser,
    RangeRegion,
    RestRegion,
    UntilRegion,
    discard,
    whitespace_numbers,
)

p = InputParser(
    [
        AfterRegion(":"),
        UntilRegion("|"),
        RangeRegion(1),
        RestRegion(),
    ],
    [
        discard,
        whitespace_numbers(set),
        discard,
        whitespace_numbers(set),
    ],
)


def part1(inp):
    sum = 0
    for line in inp:
        winning, mine = p.parse(line)
        l = len(winning.intersection(mine))
        if l > 0:
            sum += pow(2, len(winning.intersection(mine)) - 1)
    return sum


def part2(inp):
    bonus = [1] * len(inp)
    for i, line in enumerate(inp):
        winning, mine = p.parse(line)
        matches = len(winning.intersection(mine))
        for j in range(i + 1, i + matches + 1):
            bonus[j] += bonus[i]
    return sum(bonus)


test_inp = None
with open("res/day04a.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))


print("TEST DAY 04:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = None
with open("res/day04.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))

print("FINAL DAY 04:")
print(part1(inp))
print(part2(inp))
