from utils import *

def solve(input_data: str):
    lines = read_lines(input_data)
    parts = [0,0]

    ranges = [tuple(map(int, line.split('-'))) for line in lines if '-' in line]
    numbers = [int(line) for line in lines if line.isdigit()]

    # Simple brute-force check for part 1
    for i in numbers:
        for (start, end) in ranges:
            if start <= i <= end:
                parts[0] += 1
                break

    # sort on first element (second on tie) lexicographically
    ranges.sort()

    # we will combine the ranges
    combined = [list(ranges[0])]

    for start, end in ranges[1:]:
        last_start, last_end = combined[-1]

        # if the start is earlier than the end of the last added range, it still overlaps so we have to merge it
        if start <= last_end + 1:
            combined[-1][1] = max(last_end, end)
        # if not overlapping, then we can just add it as a new range
        else:
            combined.append([start, end])

    # when we know that all ranges in the combined part are non-overlapping, we can just sum their lengths
    parts[1] = sum(end - start + 1 for start, end in combined)

    return parts