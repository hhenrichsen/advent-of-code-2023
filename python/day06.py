import re
from util import (
    AfterRegion,
    InputParser,
    RestRegion,
    discard,
    whitespace_numbers,
)

p = InputParser(
    [
        (AfterRegion(":"), discard),
        (RestRegion(), whitespace_numbers()),
    ],
)


def sim(started, speed, distance, limit, goal):
    if limit <= 0:
        return 1 if distance > goal else 0
    if not started:
        return sim(False, speed + 1, distance, limit - 1, goal) + sim(
            True, speed, distance + speed, limit - 1, goal
        )
    else:
        return sim(True, speed, distance + speed, limit - 1, goal)


def part1(inp):
    sum = 1
    times = list()
    distances = list()
    for line in inp:
        if len(times) == 0:
            times = list(p.parse(line))[0]
        else:
            distances = list(p.parse(line))[0]

    for i, time in enumerate(times):
        sum *= sim(False, 0, 0, time, distances[i])

    return sum


p2 = InputParser(
    [
        (AfterRegion(":"), discard),
        (RestRegion(), lambda x: int(re.sub("\s+", "", x))),
    ]
)


def part2(inp):
    sum = 0
    times = 0
    distances = 0
    for line in inp:
        if times == 0:
            times = next(p2.parse(line))
        else:
            distances = next(p2.parse(line))

    for i in range(times):
        if ((times - i) * i) > distances:
            sum += 1

    return sum


test_inp = None
with open("res/day06a.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))

print("TEST DAY 06:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = None
with open("res/day06.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))


print("FINAL DAY 06:")
print(part1(inp))
print(part2(inp))
