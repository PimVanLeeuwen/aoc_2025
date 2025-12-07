from functools import lru_cache
from collections import deque

def solve(input_data: str):
    grid = [list(line) for line in input_data.split('\n')]
    parts = [0,0]

    q = deque()

    q.append((0, 70))
    visited = {(0, 70)}

    splits = set()

    while q:
        y, x = q.popleft()

        if (y + 1) < len(grid) and grid[y + 1][x] == '.':
            visited.add((y + 1, x))
            q.append((y + 1, x))
        elif (y + 1) < len(grid) and grid[y + 1][x] == '^':
            if not (y + 1, x - 1) in visited:
                visited.add((y + 1, x - 1))
                q.append((y + 1, x - 1))
            if not (y + 1, x + 1) in visited:
                visited.add((y + 1, x + 1))
                q.append((y + 1, x + 1))
            splits.add((y+1, x))

    @lru_cache(maxsize=None)
    def count_routes(y, x):
        if y >= len(grid) or x < 0 or x >= len(grid[0]):
            return 0
        if y == len(grid) - 1:
            return 1
        if grid[y][x] == '^':
            return count_routes(y + 1, x - 1) + count_routes(y + 1, x + 1)
        else:
            return count_routes(y + 1, x)

    parts[0] = len(splits)
    parts[1] = count_routes(0, 70)

    return parts