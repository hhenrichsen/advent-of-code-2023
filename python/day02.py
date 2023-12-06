def part1(inp):
    sum = 0
    for line in inp:
        id, rest = line.split(":")
        d = {
            "blue": 0,
            "red": 0,
            "green": 0,
        }
        games = rest.split(";")
        for game in games:
            colors = game.split(",")
            for color in colors:
                _, count_str, color = color.split(" ")
                d[color] = max(int(count_str), d[color])
        if d["blue"] <= 14 and d["green"] <= 13 and d["red"] <= 12:
            sum += int(id[5:])
    return sum


def part2(inp):
    sum = 0
    for line in inp:
        id, rest = line.split(":")
        d = {
            "blue": 0,
            "red": 0,
            "green": 0,
        }
        games = rest.split(";")
        for game in games:
            colors = game.split(",")
            for color in colors:
                _, count_str, color = color.split(" ")
                d[color] = max(int(count_str), d[color])
        sum += d["blue"] * d["red"] * d["green"]
    return sum


inp = None
with open("res/day02.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))

print(part1(inp))
print(part2(inp))
