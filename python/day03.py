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
    coords = filter_grid(
        inp,
        lambda c, x, y, grid: c.isnumeric()
        and any(
            [
                (not grid[xy[1]][xy[0]].isnumeric()) and grid[xy[1]][xy[0]] != "."
                for xy in neighbor_coords(grid, x, y, True)
            ]
        ),
    )
    seen = set()
    for coord in coords:
        if coord in seen:
            continue
        neighbors = set([coord])
        while len(d := neighbors.difference(seen)) > 0:
            for c in d:
                for xy in neighbor_coords(inp, *c):
                    if inp[xy[1]][xy[0]].isnumeric() and xy not in seen:
                        neighbors.add(xy)
                seen.add(c)
        l = sort_lambda(neighbors, lambda a, b: a[0] - b[0])
        seen.update(l)
        a = int("".join([inp[coord[1]][coord[0]] for coord in l]))
        sum += a
    return sum


def part2(inp):
    sum = 0
    stars = filter_grid(
        inp,
        lambda c, x, y, grid: c == "*"
        and len(
            [
                xy
                for xy in neighbor_coords(grid, x, y, True)
                if grid[xy[1]][xy[0]].isnumeric()
            ]
        )
        > 1,
    )
    seen = set()
    for star in stars:
        coords = set(
            [
                c
                for c in neighbor_coords(inp, *star, True)
                if inp[c[1]][c[0]].isnumeric()
            ]
        )
        seen = set()
        numbers = list()
        for coord in coords:
            if coord in seen:
                continue
            neighbors = set([coord])
            while len(d := neighbors.difference(seen)) > 0:
                for c in d:
                    for xy in neighbor_coords(inp, *c):
                        if inp[xy[1]][xy[0]].isnumeric() and xy not in seen:
                            neighbors.add(xy)
                    seen.add(c)
            l = sort_lambda(neighbors, lambda a, b: a[0] - b[0])
            a = int("".join([inp[coord[1]][coord[0]] for coord in l]))
            numbers.append(a)
        if len(numbers) == 2:
            sum += numbers[0] * numbers[1]
    return sum


test_inp = parse_grid("res/day03a.txt", lambda c, x, y: c)

print("TEST DAY 03:")
print(part1(test_inp))
print(part2(test_inp))

inp = parse_grid("res/day03.txt", lambda c, x, y: c)

print("FINAL DAY 03:")
print(part1(inp))
print(part2(inp))
