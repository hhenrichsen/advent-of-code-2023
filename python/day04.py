from functools import reduce
import re
from util import (
    Grid,
    InputParser,
    RangeRegion,
    UntilRegion,
    breadth_first_search,
    compare_x,
    compare_y,
    either,
    eq,
    intersect_strings,
    inv,
    is_in,
    ne,
    not_in,
    segmented_lines,
    sort_lambda,
    stripped_lines,
    windows,
)

grid = False


def part1(inp):
    sum = 0
    for line in inp:
        _, rest = line.split(":")
        numbers_str, others_str = rest.split(" | ")
        winning = set(
            map(int, filter(str.isnumeric, re.split("\s+", numbers_str.strip())))
        )
        mine = set(map(int, filter(str.isnumeric, re.split("\s+", others_str.strip()))))
        l = len(winning.intersection(mine))
        if l > 0:
            sum += pow(2, len(winning.intersection(mine)) - 1)
    return sum


def part2(inp):
    bonus = [1] * len(inp)
    for i, line in enumerate(inp):
        print(bonus)
        _, rest = line.split(":")
        numbers_str, others_str = rest.split(" | ")
        winning = set(
            map(int, filter(str.isnumeric, re.split("\s+", numbers_str.strip())))
        )
        mine = set(map(int, filter(str.isnumeric, re.split("\s+", others_str.strip()))))
        matches = len(winning.intersection(mine))
        for j in range(i + 1, i + matches + 1):
            bonus[j] += bonus[i]
    return sum(bonus)


if not grid:
    test_inp = None
    with open("res/day04a.txt") as f:
        test_inp = list(map(lambda s: s.strip(), f.readlines()))
else:
    test_inp = Grid.read("res/day04a.txt")


print("TEST DAY 04:")
# print(part1(test_inp))
print(part2(test_inp))
print()

if not grid:
    inp = None
    with open("res/day04.txt") as f:
        inp = list(map(lambda s: s.strip(), f.readlines()))
else:
    inp = Grid.read("res/day04.txt")

print("FINAL DAY 04:")
# print(part1(inp))
print(part2(inp))
