from dataclasses import dataclass

from utils import *

@dataclass
class Machine:
    lights: str
    button_wirings: list
    joltage_requirements: list

def solve(input_data: str):
    lines = read_lines(input_data)
    devices = {}
    for line in lines:
        name, rest = line.split(':')
        rest_list = rest.strip().split(' ')
        devices[name.strip()] = rest_list

    parts = [0,0]

    # Part 1 BFS to find all reachable devices from 'you' to 'out'
    q = deque()
    q.append('you')
    while q:
        m = q.popleft()
        for t in devices[m]:
            if t == 'out':
                parts[0] += 1
                continue
            q.append(t)

    # Part 2 DFS with memoization to count paths from 'svr' to 'out' visiting 'dac' and 'fft'
    memo = {}

    def count_paths(current_node, visited_required):
        if current_node == 'out':
            return 1 if visited_required == {'dac', 'fft'} else 0

        state = (current_node, visited_required)
        if state in memo:
            return memo[state]

        total_paths = 0
        for neighbor in devices[current_node]:
            if neighbor in {'dac', 'fft'}:
                new_visited_required = visited_required.union({neighbor})
            else:
                new_visited_required = visited_required

            total_paths += count_paths(neighbor, new_visited_required)

        memo[state] = total_paths
        return total_paths

    parts[1] = count_paths('svr', frozenset())

    return parts