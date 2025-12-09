from dataclasses import dataclass
from shapely.geometry import Polygon
from shapely.prepared import prep
from itertools import product

from utils import *


@dataclass
class Point:
    x: int = 0
    y: int = 0


def solve(input_data: str):
    parts = [0, 0]
    points = [Point(*map(int, line.strip().split(','))) for line in read_lines(input_data)]
    poly = prep(Polygon([tuple(map(int, line.strip().split(','))) for line in read_lines(input_data)]))

    # Part 1, just compute area
    for p1, p2 in product(points, points):
        area = (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)
        if area > parts[0]:
            parts[0] = area

    # Part 2, compute rectangle using Shapely and check if the created polygon covers it
    for p1, p2 in product(points, points):
        min_x, max_x = min(p1.x, p2.x), max(p1.x, p2.x)
        min_y, max_y = min(p1.y, p2.y), max(p1.y, p2.y)
        rect = Polygon([(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)])
        if poly.covers(rect):
            parts[1] = max(parts[1], (max_x - min_x + 1) * (max_y - min_y + 1))

    return parts
