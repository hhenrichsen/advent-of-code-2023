from statistics import mode


def score(a):
    am = dict()
    value = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    for c in a[0]:
        am[c] = am.get(c, 0) + 1

    m = sorted(am.values())

    mh = "".join((map(lambda x: chr(ord("2") + value.index(x)), a[0])))

    if m == [5]:
        return (6, mh)
    if m == [1, 4]:
        return (5, mh)
    if m == [2, 3]:
        return (4, mh)
    if m == [1, 1, 3]:
        return (3, mh)
    if m == [1, 2, 2]:
        return (2, mh)
    if m == [1, 1, 1, 2]:
        return (1, mh)
    if m == [1, 1, 1, 1, 1]:
        return (0, mh)


def score2(a):
    am = dict()
    value = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    no_j = a[0].replace("J", "")
    if len(no_j) == 0:
        no_j = "11111"
    common = mode(no_j)
    for c in a[0]:
        if c == "J":
            am[common] = am.get(common, 0) + 1
        else:
            am[c] = am.get(c, 0) + 1

    m = sorted(am.values())

    mh = "".join((map(lambda x: chr(ord("1") + value.index(x)), a[0])))

    if m == [5]:
        return (6, mh)
    if m == [1, 4]:
        return (5, mh)
    if m == [2, 3]:
        return (4, mh)
    if m == [1, 1, 3]:
        return (3, mh)
    if m == [1, 2, 2]:
        return (2, mh)
    if m == [1, 1, 1, 2]:
        return (1, mh)
    if m == [1, 1, 1, 1, 1]:
        return (0, mh)


def part1(inp: list[str]):
    sum = 0
    lines = []
    for line in inp:
        card, bid_str = line.split(" ")
        bid = int(bid_str.strip())
        lines.append((card, bid))
    s = sorted(lines, key=score, reverse=True)
    for i, c in enumerate(s):
        sum += (len(s) - i) * c[1]
    return sum


def part2(inp):
    sum = 0
    lines = []
    for line in inp:
        card, bid_str = line.split(" ")
        bid = int(bid_str.strip())
        lines.append((card, bid))
    s = sorted(lines, key=score2, reverse=True)
    for i, c in enumerate(s):
        sum += (len(s) - i) * c[1]
    return sum


test_inp = None
with open("res/day07a.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))


print("TEST DAY 07:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = None
with open("res/day07.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))

print("FINAL DAY 07:")
print(part1(inp))
print(part2(inp))
