import sys

_, day = sys.argv

with open(f"./res/day{day}.txt", "w") as f:
    f.write("")

with open(f"./res/day{day}a.txt", "w") as f:
    f.write("")

with open(f"./python/day{day}.py", "w") as f:
    f.write(
        f"""
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
        ...
    return sum


def part2(inp):
    sum = 0
    for line in inp:
        ...
    return sum

if not grid:
    test_inp = None
    with open("res/day{day}a.txt") as f:
        test_inp = list(map(lambda s: s.strip(), f.readlines()))
else:
    test_inp = Grid.read("res/day{day}a.txt")


print("TEST DAY {day}:")
print(part1(test_inp))
print(part2(test_inp))
print()

if not grid:
    inp = None
    with open("res/day{day}.txt") as f:
        test_inp = list(map(lambda s: s.strip(), f.readlines()))
else:
    inp = Grid.read("res/day{day}.txt")


print("FINAL DAY {day}:")
print(part1(inp))
print(part2(inp))
    """
    )
