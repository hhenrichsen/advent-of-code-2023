from copy import deepcopy, copy
from util import (
    Grid,
    Interval,
)


def part1(inp: list[str]):
    steps = [[]]
    transform_groups = []
    for line in inp:
        if len(line) == 0:
            continue
        elif len(steps[0]) == 0:
            steps[0] = list(map(int, map(str.strip, line.split(":")[1].split(" ")[1:])))
        elif line.endswith(":"):
            transform_groups.append([])
        else:
            target, source, length = list(map(int, line.split(" ")))
            delta = target - source
            transform_groups[-1].append((target, source, length, delta))

    for transform_group in transform_groups:
        orig = steps[-1]
        res = copy(steps[-1])
        for target, source, length, delta in transform_group:
            for i, item in enumerate(orig):
                ti = (
                    (item + delta)
                    if item >= source and item < source + length
                    else item
                )
                if item != ti:
                    res[i] = ti
        steps.append(res)
    return min(steps[-1])


def part2(inp):
    steps = [[]]
    transform_groups = []
    for line in inp:
        if len(line) == 0:
            continue
        elif len(steps[0]) == 0:
            il = list(map(int, map(str.strip, line.split(":")[1].split(" ")[1:])))
            steps[0] = [(il[i], il[i] + il[i + 1]) for i in range(0, len(il), 2)]
        elif line.endswith(":"):
            transform_groups.append([])
        else:
            target, source, length = list(map(int, line.split(" ")))
            delta = target - source
            transform_groups[-1].append((target, source, length, delta))

    for group in transform_groups:
        curr = deepcopy(steps[-1])
        solve = []
        for transform in group:
            target, source, length, delta = transform
            iv = Interval(source, source + length)
            for step_index, step in enumerate(curr):
                if step == None:
                    continue
                step_interval = Interval(*step)
                if (
                    intersect_intervals := step_interval.intersection(iv)
                ) is not None and len(intersect_intervals) > 0:
                    curr[step_index] = None
                    for res in step_interval.difference(intersect_intervals):
                        if (isi := step_interval.intersection(res)) is not None and len(
                            isi
                        ) > 0:
                            curr.append((isi.start, isi.end))
                    solve.append(
                        (
                            intersect_intervals.start + delta,
                            intersect_intervals.end + delta,
                        )
                    )
        solve.extend([c for c in curr if c is not None])
        steps.append(solve)

    return min(map(lambda x: x[0], steps[-1]))


test_inp = None
with open("res/day05a.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))


print("TEST DAY 05:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = None
with open("res/day05.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))


print("FINAL DAY 05:")
print(part1(inp))
print(part2(inp))
