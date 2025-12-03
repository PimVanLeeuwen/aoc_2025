from utils import *

def solve(input_data: str):
    lines = read_lines(input_data)
    parts = [0,0]

    for line in lines:

        # Part 1, brute force
        digits = list(line.strip())
        parts[0] += max(int(digits[i] + digits[j]) for i in range(len(digits)) for j in range(i + 1, len(digits)))

        # Part 2, take the max number, from the available numbers, greedy approach
        n = len(digits)
        result = []
        start = 0
        for k in range(12, 0, -1):
            # get the largest digit, index from the subarray digits[start:n - k + 1] (we still need to remainder for other digits)
            largest = max(digits[start:n - k + 1])
            i = digits.index(largest, start, n - k + 1)

            # Append that digit
            result.append(largest)
            start = i + 1
        parts[1] += int(''.join(result))

    return parts