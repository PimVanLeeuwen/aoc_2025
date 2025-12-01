from utils import *

def solve(input_data: str):
    """Solve both parts of the Advent of Code Day"""

    # Variables
    lines = read_lines(input_data)
    dial = 50
    part_1 = 0
    part_2 = 0

    # Part 1 solution
    # Pretty basic math
    for line in lines:
        direction, distance = line[0], int(line[1:])

        if direction == 'L':
            dial = (dial - distance) % 100
        else:
            dial = (dial + distance) % 100

        if dial == 0:
            part_1 += 1

    # Reset for part 2
    dial = 50

    # Part 2 solution
    # Math was not working at 6AM, so we simulate the dial turn by turn
    for line in lines:
        direction, distance = line[0], int(line[1:])

        while distance > 0:
            if direction == 'L':
                dial -= 1
                distance -= 1
                if dial == 0:
                    part_2 += 1
                if dial < 0:
                    dial = 99
            else:
                dial += 1
                distance -= 1
                if dial == 100:
                    part_2 += 1
                    dial = 0

    return part_1, part_2