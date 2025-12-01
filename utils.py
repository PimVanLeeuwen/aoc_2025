import re
from math import prod

# Yield successive n-sized chunks from lst.
def array_chunks(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

# Return all 8-directional neighbors for (r, c) in a grid.
def neighbors_8(y, x, rows, cols):
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = y + dr, x + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbors.append((nr, nc))
    return neighbors

# Extract all integers from a string.
def extract_ints(s):
    return list(map(int, re.findall(r'-?\d+', s)))

# product of all items in a list
def prod_list(lst):
    return prod(lst)

# Manhattan distance between points a and b.
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def read_input(day: int) -> str:
    with open(f'inputs/day{day:02d}.txt', 'r') as file:
        return file.read()

#read input lines
def read_lines(lines):
    return lines.strip().split('\n')

# Flatten a 2D list
def flatten(matrix):
    return [item for row in matrix for item in row]

# Transpose a 2D list
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# Rotate a 2D list 90 degrees clockwise
def rotate_90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

# utils.py

def dfs_grid(grid, start, is_valid=lambda r, c: True):
    rows, cols = len(grid), len(grid[0])
    stack = [start]
    visited = set()
    while stack:
        r, c = stack.pop()
        if (r, c) in visited or not (0 <= r < rows and 0 <= c < cols) or not is_valid(r, c):
            continue
        visited.add((r, c))
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            stack.append((r+dr, c+dc))
    return visited

# Extract all single uppercase letters from a string.
def extract_letters(s):
    return re.findall(r'\b([A-Z])\b', s)

from collections import deque
def bfs_grid(grid, start, is_valid=lambda r, c: True):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = {start}
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r+dr, c+dc
            if (0 <= nr < rows and 0 <= nc < cols and
                (nr, nc) not in visited and is_valid(nr, nc)):
                visited.add((nr, nc))
                queue.append((nr, nc))
    return visited

# Example usages
# Only visit open cells (value == 0)
# def is_open(r, c):
#     return grid[r][c] == 0
#
# start = (0, 0)
#
# dfs_result = dfs_grid(grid, start, is_open)
# bfs_result = bfs_grid(grid, start, is_open)
#
# print("DFS visited:", dfs_result)
# print("BFS visited:", bfs_result)
