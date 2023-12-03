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
    sort_lambda,
    intersect_strings,
    windows,
    stripped_lines,
    segmented_lines,
    breadth_first_search,
    parse_grid,
    map_grid,
    filter_grid,
    neighbor_coords,
    flood,
)

            
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


test_inp = None
with open("res/day{day}a.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))

print("TEST DAY {day}:")
print(part1(test_inp))
print(part2(test_inp))

inp = None
with open("res/day{day}.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))

print("FINAL DAY {day}:")
print(part1(inp))
print(part2(inp))
    """
    )
