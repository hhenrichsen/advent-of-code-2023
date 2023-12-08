from math import lcm


def part1(inp):
    sum = 0

    order = list(map(lambda a: 1 if a == "R" else 0, inp[0]))
    m = dict()
    for line in inp[2:]:
        k, _, l, r = (
            line.replace(",", "")
            .replace("=", "")
            .replace("(", "")
            .replace(")", "")
            .split(" ")
        )
        m[k] = (l, r)
    curr = "AAA"
    while curr != "ZZZ":
        for o in order:
            curr = m[curr][o]
            sum += 1
            if curr == "ZZZ":
                break
    return sum


def part2(inp):
    order = list(map(lambda a: 1 if a == "R" else 0, inp[0]))
    m = dict()
    starting = dict()
    for line in inp[2:]:
        k, _, l, r = (
            line.replace(",", "")
            .replace("=", "")
            .replace("(", "")
            .replace(")", "")
            .split(" ")
        )
        m[k] = (l, r)
        if k.endswith("A"):
            starting[k] = k

    seen = dict([(k, 0) for k in starting])
    curr = starting
    while len(curr) > 0:
        for o in order:
            remove = []
            for k, v in curr.items():
                curr[k] = m[v][o]
                if curr[k].endswith("Z"):
                    remove.append(k)
                seen[k] += 1
            for r in remove:
                del curr[r]
    print(list(seen.values()))
    return lcm(*seen.values())


test_inp = None
with open("res/day08b.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))

test_inp2 = None
with open("res/day08c.txt") as f:
    test_inp2 = list(map(lambda s: s.strip(), f.readlines()))

print("TEST DAY 08:")
print(part1(test_inp))
print(part2(test_inp2))
print()

inp = None
with open("res/day08.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))

print("FINAL DAY 08:")
print(part1(inp))
print(part2(inp))
