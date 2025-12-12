from utils import read_lines

def solve(input_data):
    parts = [0,0]

    regions_part = read_lines(input_data.split("\n\n")[-1])
    regions = []
    for line in regions_part:
        left, right = line.split(":")
        w, h = map(int, left.split("x"))
        counts = list(map(int, right.strip().split()))
        regions.append((w, h, counts))

    # naive check for part 1
    for w, h, counts in regions:
        total_presents = sum(counts)

        capacity = (w // 3) * (h // 3)

        if total_presents <= capacity:
            parts[0] += 1

    return parts
