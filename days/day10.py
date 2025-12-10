from dataclasses import dataclass
from scipy.optimize import linprog
from utils import *

@dataclass
class Machine:
    lights: str
    button_wirings: list
    joltage_requirements: list

# What a horrible input format...
def parse_machine_line(line):
    lights = re.search(r'\[([^]]+)]', line).group(1)
    button_wirings = [list(map(int, wiring.split(','))) for wiring in re.findall(r'\(([^)]+)\)', line)]
    joltage_requirements = list(map(int, re.search(r'\{([^}]+)}', line).group(1).split(',')))
    return Machine(lights, button_wirings, joltage_requirements)

def min_presses_part_1(lights, button_wirings):
    target = tuple(1 if c == '#' else 0 for c in lights)
    start = tuple([0] * len(lights))

    if target == start:
        return 0

    q = deque([(start, 0)])
    visited = {start}

    while q:
        current_state, presses = q.popleft()

        # add each possible press of a button
        for wiring in button_wirings:
            next_state = list(current_state)
            # Flip the lights connected to this button
            for i in wiring:
                next_state[i] = 1 - next_state[i]

            next_state = tuple(next_state)

            # done
            if next_state == target:
                return presses + 1

            # skip visited
            if next_state not in visited:
                visited.add(next_state)
                q.append((next_state, presses + 1))
    return -1


def min_presses_part_2(joltage_requirements, button_wirings):
    n = len(joltage_requirements)
    m = len(button_wirings)

    #
    # Example: 2 counters, 2 buttons
    # top vector denotes which buttons are pressed how many times (minimize this)
    # left matrix is fixed and denotes which buttons affect which counters
    # result vector denotes required joltages (fixed as well)
    #
    #                [ c = 0 ]
    #                [ c = 1 ]
    # [ A_eq = 1 0 ] [ b_eq = 0 ]
    # [ A_eq = 0 1 ] [ b_eq = 1 ]
    #

    c = [1] * m

    # which buttons affect which counters
    # A_eq[i, j] = 1 if button j affects counter i, else 0
    a_eq = [[0 for _ in range(m)] for _ in range(n)]
    for j, wiring in enumerate(button_wirings):
        for i in wiring:
            a_eq[i][j] += 1

    # required joltages (fixed as well)
    b_eq = joltage_requirements

    # Bounds for variables (you cannot press negative times)
    bounds = (0, None)

    # Solve the integer linear programming problem
    res = linprog(c, A_eq=a_eq, b_eq=b_eq, bounds=bounds, integrality=1, method='highs')
    print(res)

    return int(res.fun)


def solve(input_data: str):
    lines = [parse_machine_line(line) for line in read_lines(input_data)]

    parts = [0,0]

    parts[0] = sum(min_presses_part_1(machine.lights, machine.button_wirings) for machine in lines)
    parts[1] = sum(min_presses_part_2(machine.joltage_requirements, machine.button_wirings) for machine in lines)

    return parts