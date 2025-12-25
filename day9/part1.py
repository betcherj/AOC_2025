import os
import math

NUM_JUNCTIONS = 1000

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    data = f.read().splitlines()
    corners = [(int(x), int(y)) for x, y in (line.split(',') for line in data)]

def narrow_candidates(points):
    min_x = min(c[0] for c in points)
    max_x = max(c[0] for c in points)
    min_y = min(c[1] for c in points)
    max_y = max(c[1] for c in points)
    return min_x, max_x, min_y, max_y

def calculate_area(point1, point2):
    return (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)

def find_largest(corners):
    largest_area = 0
    for i in range(len(corners)):
        for j in range(i+1, len(corners)):
            area = calculate_area(corners[i], corners[j])
            if area > largest_area:
                print(f"Found max area {area} between points {corners[i]} and {corners[j]}")
                largest_area = area
    return largest_area

if __name__ == "__main__":
    print(find_largest(corners))