from util import Grid, sort_lambda, ne, not_in, inv, compare_x


def part1(inp: Grid):
    sum = 0
    numbers = inp.filter(
        lambda item: item.data.isnumeric()
        and item.count_neighbor_data(
            [inv(str.isnumeric), ne(".")],
            diagonal=True,
        )
        > 0
    )

    seen = set()
    for number in numbers:
        if number in seen:
            continue
        neighbors = set([number])
        while len(d := neighbors.difference(seen)) > 0:
            for c in d:
                neighbors.update(
                    c.filter_neighbor_data(
                        [str.isnumeric, not_in(seen)],
                        diagonal=True,
                    )
                )
                seen.add(c)
        l = sort_lambda(neighbors, compare_x)
        seen.update(l)
        a = int("".join([inp[coord.x, coord.y]() for coord in l]))
        sum += a
    return sum


def part2(inp: Grid):
    sum = 0
    stars = inp.filter(
        lambda c: c() == "*" and c.count_neighbor_data(str.isnumeric, diagonal=True) > 1
    )

    for star in stars:
        neighboring_numbers = set(
            star.filter_neighbor_data(str.isnumeric, diagonal=True)
        )
        seen = set()
        numbers = list()
        for neighbor in neighboring_numbers:
            if neighbor in seen:
                continue
            neighbors = set([neighbor])
            while len(d := neighbors.difference(seen)) > 0:
                for c in d:
                    neighbors.update(
                        c.filter_neighbor_data(
                            [str.isnumeric, not_in(seen)],
                            diagonal=True,
                        )
                    )
                    seen.add(c)
            l = sort_lambda(neighbors, compare_x)
            a = int("".join([inp[coord.x, coord.y]() for coord in l]))
            numbers.append(a)
        if len(numbers) == 2:
            sum += numbers[0] * numbers[1]
    return sum


test_inp = Grid.read("res/day03a.txt")

print("TEST DAY 03:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = Grid.read("res/day03.txt")

print("FINAL DAY 03:")
print(part1(inp))
print(part2(inp))
