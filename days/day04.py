from utils import *
from itertools import product

def solve(input_data: str):
    grid = [list(line) for line in input_data.split('\n')]
    parts = [0,0]

    # Part 1
    for y, x in product(range(len(grid)), range(len(grid[0]))):
        rolls = sum(1 for dy, dx in neighbors_8(y, x, len(grid), len(grid[0])) if grid[dy][dx] == '@')
        if grid[y][x] == '@' and rolls < 4:
            parts[0] += 1

    # Part 2
    while True:
        changed = False
        for y, x in product(range(len(grid)), range(len(grid[0]))):
            rolls = sum(1 for dy, dx in neighbors_8(y, x, len(grid), len(grid[0])) if grid[dy][dx] == '@')
            if grid[y][x] == '@' and rolls < 4:
                grid[y][x] = '.'
                parts[1] += 1
                changed = True
        if not changed:
            break

    return parts