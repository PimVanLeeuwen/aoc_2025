import sys
import time
from importlib import import_module

from utils import read_input


def run_day(day_to_run: int):
    input_data = read_input(day_to_run)
    day_module = import_module(f'days.day{day_to_run:02d}')
    start = time.time()
    result = day_module.solve(input_data)
    elapsed = time.time() - start
    print(f'\033[92mDay {day_to_run:02d} result ({elapsed:.3f}s): \n {result}\033[0m')

if __name__ == '__main__':
    day = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    run_day(day)
