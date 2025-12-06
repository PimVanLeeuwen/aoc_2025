from utils import *

def solve(input_data: str):
    # Parsed version for part 1
    lines = [list(r for r in l.split(" ") if r ) for l in read_lines(input_data)]

    # String version for part 2
    lines_string = [line.rstrip('\n') for line in input_data.splitlines() if line.strip()]
    grid = [line.ljust(max(len(line) for line in lines_string)) for line in lines_string]

    parts = [0,0]

    # Part 1 easy adding and multiplying
    for i in range(1000):
        parts[0] += prod(int(lines[r][i]) for r in range(4)) if lines[4][i] == '*' else sum(int(lines[r][i]) for r in range(4))

    # Part 2 loop over string
    i, p = 0, 0
    while i < len(grid[0]):
        # all are empty , continue
        if all(grid[r][i] == ' ' for r in range(5)):
            i += 1
            continue

        # Collect columns for this problem (all columns between empty columns)
        p_cols = []
        while i < len(grid[0]) and not all(grid[r][i] == ' ' for r in range(4)):
            p_cols.append(i)
            i += 1

        # Process columns right-to-left
        numbers = []
        for c in reversed(p_cols):
            num = ''.join(grid[r][c] for r in range(4)).strip()
            if num:
                numbers.append(int(num))

        # reuse logic from part 1
        parts[1] += sum(numbers) if lines[4][p] == '+' else prod(numbers)

        # next problem
        p += 1

    return parts